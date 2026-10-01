# Wiring (bench, V1)

```text
Analog 3V3 (P9_3) -> AD8232 3.3V, ADS1115 VDD
GND star point    -> AD8232 GND, ADS1115 GND, PCM5102A GND
ADS1115 SDA/SCL   -> BBAI I2C pins (see pinout.md), ADDR -> GND (0x48)
AD8232 OUTPUT     -> 100-330 ohm -> ADS1115 AIN0
AD8232 LO+/LO-    -> 100k -> BBAI GPIO (optional)
```

PCM5102A (3-wire I2S): SCK->GND, FMT->GND, FLT->GND, DEMP->GND, XSMT->3.3V. Output to active speaker only.
