"""ADS1115 single-shot driver using smbus2 (3.3 V logic only)."""
import time

REG_CONVERSION = 0x00
REG_CONFIG = 0x01

_MUX = {0: 0b100, 1: 0b101, 2: 0b110, 3: 0b111}
_PGA = {
    # gain: (config bits, full-scale volts)
    2 / 3: (0b000, 6.144),
    1: (0b001, 4.096),
    2: (0b010, 2.048),
    4: (0b011, 1.024),
    8: (0b100, 0.512),
    16: (0b101, 0.256),
}
_DR = {8: 0b000, 16: 0b001, 32: 0b010, 64: 0b011,
       128: 0b100, 250: 0b101, 475: 0b110, 860: 0b111}


class ADS1115:
    def __init__(self, bus=4, address=0x48, channel=0, gain=1, sample_rate=250):
        from smbus2 import SMBus  # imported lazily so tests run without hardware
        if channel not in _MUX:
            raise ValueError("channel must be 0-3")
        if gain not in _PGA:
            raise ValueError("unsupported gain")
        if sample_rate not in _DR:
            raise ValueError("unsupported sample rate")
        self.bus = SMBus(bus)
        self.address = address
        self.full_scale = _PGA[gain][1]
        self.sample_rate = sample_rate
        self._config = (
            (1 << 15) | (_MUX[channel] << 12) | (_PGA[gain][0] << 9)
            | (1 << 8) | (_DR[sample_rate] << 5) | 0b11  # comparator off
        )
        self._timeout = 2.0 / sample_rate + 0.005

    def read_raw(self):
        cfg = self._config
        self.bus.write_i2c_block_data(
            self.address, REG_CONFIG, [(cfg >> 8) & 0xFF, cfg & 0xFF])
        deadline = time.monotonic() + self._timeout
        while time.monotonic() < deadline:
            hi, _ = self.bus.read_i2c_block_data(self.address, REG_CONFIG, 2)
            if hi & 0x80:  # OS bit: conversion done
                break
        hi, lo = self.bus.read_i2c_block_data(self.address, REG_CONVERSION, 2)
        value = (hi << 8) | lo
        return value - 65536 if value & 0x8000 else value

    def to_volts(self, raw):
        return raw * self.full_scale / 32768.0

    def close(self):
        self.bus.close()
