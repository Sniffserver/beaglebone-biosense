# Pinout (VERIFY BEFORE WIRING)

BBAI pinmux comes from the boot-time device tree. Nothing here is final until checked against your image's DTS (`am572x-bone-common-univ.dtsi`, `am5729-beagleboneai.dts`) and the BBAI SRM.

| Signal | BBAI pin | Status |
|---|---|---|
| 3.3 V | P9_3 / P9_4 | verified by convention |
| GND | P9_1 / P9_2 | verified by convention |
| I2C SCL | P9_17 (candidate) | VERIFY bus number |
| I2C SDA | P9_18 (candidate) | VERIFY bus number |
| LO+ / LO- | any free GPIO | pick later |
| McASP BCK/LRCK/DIN | TBD | needs DTS audit (HDMI conflict) |

P9_19/P9_20 are normally kept for cape EEPROM detection.

Find the bus: `i2cdetect -l` and `ls /sys/class/i2c-dev/`.
