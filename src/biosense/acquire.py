"""Acquisition loop: read ADS1115, log raw + timestamp + flags to CSV segments."""
import argparse
import csv
import os
import time
from datetime import datetime, timezone

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    import tomli as tomllib

from .adc import ADS1115
from .quality import flags


def load_config(path):
    with open(path, "rb") as f:
        return tomllib.load(f)


def run(cfg):
    a, s, q = cfg["adc"], cfg["storage"], cfg["quality"]
    adc = ADS1115(a["i2c_bus"], a["address"], a["channel"], a["gain"], a["sample_rate"])
    period_ns = int(1e9 / a["sample_rate"])
    expected_ms = 1000.0 / a["sample_rate"]
    os.makedirs(s["output_dir"], exist_ok=True)
    try:
        while True:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            path = os.path.join(s["output_dir"], f"ecg_{stamp}.csv")
            seg_end = time.monotonic() + s["segment_seconds"]
            with open(path, "w", newline="") as fh:
                w = csv.writer(fh)
                w.writerow(["t_ns", "raw", "volts", "flags"])
                next_t = time.monotonic_ns()
                last_t = None
                while time.monotonic() < seg_end:
                    raw = adc.read_raw()
                    t = time.monotonic_ns()
                    jit = abs((t - last_t) / 1e6 - expected_ms) if last_t else None
                    last_t = t
                    w.writerow([t, raw, f"{adc.to_volts(raw):.6f}",
                                "|".join(flags(raw, jit, q["max_jitter_ms"]))])
                    next_t += period_ns
                    delay = (next_t - time.monotonic_ns()) / 1e9
                    if delay > 0:
                        time.sleep(delay)
                    else:
                        next_t = time.monotonic_ns()
    except KeyboardInterrupt:
        pass
    finally:
        adc.close()


def main():
    p = argparse.ArgumentParser(description="biosense acquisition (experimental, non-diagnostic)")
    p.add_argument("--config", default="config/config.toml")
    run(load_config(p.parse_args().config))


if __name__ == "__main__":
    main()
