# Architecture

```text
adc.py (ADS1115) -> acquire.py -> quality.py -> CSV segments
                                 \-> (later) ring buffer -> WebSocket -> web/
filters.py: view-only (raw is always stored)
later: audio.py (ALSA sonification), server.py (FastAPI)
```

Principles: raw first, timestamps from `time.monotonic_ns()`, quality flags on every sample, filters never overwrite raw.

Userspace `smbus2` is the V1 path. Kernel IIO node and PRU are optional later steps; never use both on the same device at once.
