# beaglebone-biosense

Experimental biosignal lab on **BeagleBone AI (AM5729)**: AD8232 ECG front end -> ADS1115 ADC -> local logging -> live dashboard, plus PCM5102A I2S audio.

> **NOT a medical device.** Experimental, non-diagnostic. Never use for health decisions.

## TL;DR (30 seconds)

1. Read [`docs/safety.md`](docs/safety.md) (2 min).
2. Open [`START-HERE.md`](START-HERE.md) - it is the only checklist you need.
3. Open [`NEXT.md`](NEXT.md) - it holds exactly ONE next action.

## What is in the box

| Part | Job |
|---|---|
| BeagleBone AI | Host (3.3 V logic) |
| AD8232 | ECG analog front end |
| ADS1115 | 16-bit I2C ADC, addr 0x48 |
| PCM5102A | I2S DAC, line-level audio |
| AD620 | Bench experiments only (`experiments/ad620/`) |

```text
Electrodes -> AD8232 -> 100-330 ohm -> ADS1115 AIN0 --I2C--> BBAI
BBAI -> acquire.py -> CSV segments (+ later SQLite, WebSocket)
BBAI McASP -> PCM5102A -> active speaker
```

## Status

| Milestone | State |
|---|---|
| Repo scaffold, docs, CI | done |
| ADS1115 userspace driver + CSV logger | draft, untested on hardware |
| Dashboard (FastAPI + WebSocket) | todo |
| PCM5102A McASP overlay | todo |
| PRU timing (optional) | todo |

## BBAI gotchas

- Pinmux = **device tree at boot**, not `config-pin`.
- ADS1115 runs at **3.3 V**.
- On-chip ADC range is believed to be 1.8 V - verify in the SRM before use. Do not feed AD8232 into it directly.
- Audio: McASP + ALSA. PRU is not for I2S.
- Verify every pin against YOUR image's DTS.

## Quick start

```bash
git clone https://github.com/Sniffserver/beaglebone-biosense.git
cd beaglebone-biosense
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp config/config.example.toml config/config.toml   # edit i2c_bus
sudo i2cdetect -y -r <bus>                           # expect 0x48
PYTHONPATH=src python -m biosense.acquire --config config/config.toml
```

Tests (no hardware needed): `PYTHONPATH=src pytest`

## Layout

```text
docs/        safety, pinout, wiring, bring-up, architecture
config/      config.example.toml
dts/         device tree overlays (todo)
firmware/pru optional PRU C code
src/biosense Python package
web/         dashboard (todo)
systemd/     service unit
scripts/     helper scripts
tests/       unit tests
experiments/ AD620 bench work
data/        runtime output (git-ignored)
```

## Licence

None chosen yet. Add a `LICENSE` file (MIT or Apache-2.0 suggested) before sharing code.
