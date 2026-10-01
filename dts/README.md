# Device tree overlays

Todo: `BB-BIOSENSE-I2C-ADS1115.dts`, `BB-BIOSENSE-MCASP-PCM5102A.dts`.

Write them only after checking your image's DTS. Build: `dtc -@ -I dts -O dtb -o X.dtbo X.dts`, copy to `/lib/firmware/`, enable in `/boot/uEnv.txt`.
