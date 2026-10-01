# START HERE

One page. Tick boxes. Skip nothing in Phase 0.

## Phase 0 - Safety (no wires yet)
- [ ] Read `docs/safety.md`
- [ ] Battery power plan for any human-electrode test
- [ ] Signal generator or ECG simulator ready

## Phase 1 - Board alive
- [ ] BBAI boots, SSH works
- [ ] `sudo apt install -y i2c-tools python3-venv git alsa-utils`
- [ ] `uname -r` and `cat /boot/uEnv.txt` saved into `docs/board-notes.md`

## Phase 2 - ADS1115 only
- [ ] Pick I2C bus from your DTS (see `docs/pinout.md`)
- [ ] Wire VDD=3.3V, GND, SDA, SCL, ADDR=GND
- [ ] `sudo i2cdetect -y -r <bus>` shows `48`
- [ ] Feed 0-3.3 V from a pot/divider to AIN0; run `acquire.py`
- [ ] Check the CSV: values change, jitter is reported

## Phase 3 - AD8232 with a generator (not a person)
- [ ] Power AD8232 at 3.3 V
- [ ] OUT -> 100-330 ohm -> AIN0
- [ ] Inject a small test signal, see it in CSV

## Phase 4 - Dashboard, then audio
- [ ] FastAPI + WebSocket (todo)
- [ ] PCM5102A overlay + `speaker-test` (todo)

## Rules that save you hours
- One change at a time. Commit after each working step.
- Stuck >20 min? Write the symptom in `NEXT.md`, take a break.
- Never debug electrodes and software at the same time.
