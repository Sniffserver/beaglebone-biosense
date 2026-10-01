# Safety

Experimental and non-diagnostic. Not a medical device.

## Hard rules
- Human electrodes only with **battery power** and nothing else grounded connected (no USB to PC, Ethernet, HDMI, bench PSU).
- Test with a signal generator or ECG simulator first.
- Keep the AD8232 right-leg-drive/reference path current-limited per the Analog Devices datasheet.
- AD620 module is never connected to a person in this project.
- Dashboard binds to `127.0.0.1`; remote access only via VPN (WireGuard/Tailscale).

## Ground loops
- One star ground point: AD8232, ADS1115, PCM5102A grounds meet there with short wires.
- Keep audio output wiring away from electrode leads.
- Audio goes to an active speaker or line input, never straight to a passive speaker or headphones.
