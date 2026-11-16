# FeiyuTech G6 Plus OLED repair experiment

[Español](README.es.md)

An experimental firmware patch for a **FeiyuTech G6 Plus** with a replacement 0.42-inch 72×40 OLED. The owner reported that the upper part went dark after a few seconds, with a brief full-screen flash. After installing the patched **AJB/keyboard Sony V1.10** firmware, the owner reported the screen works correctly. This is one successful report, not a compatibility guarantee.

The replacement flex was marked `V01870-MF1-B`; its actual controller is unknown. SSD1315 is a working hypothesis. The original display flex was marked `HP7240-01`. The issue predates the replacement screen's patch and the original screen failed years after the previous firmware update.

## Before starting

- This modifies the keyboard/AJB board firmware, **not** the GIMBAL firmware. Other versions and variants have not been tested. Verify your model and firmware variant before proceeding.
- Firmware updates can fail and may leave the device unusable. The manufacturer documents updating over a USB-to-serial adapter; recovery after a failed flash has not been demonstrated. Keep the matching official firmware and updater available.
- This repository does not contain FeiyuTech firmware or the Windows updater. Obtain the official **Sony AJB V1.10 WIRE** file separately. The generator only accepts the exact SHA-256 below; if your download does not match, do not use this patch.
- Download page and official procedure: [FeiyuTech G6 Plus downloads](https://www.feiyu-tech.com/g6-plus/down.html). Availability and exact variant filenames may change; the download page has not been confirmed to provide the exact matching Sony WIRE file.

## Generate the patched file

Install Python 3, then in a terminal run:

```powershell
python patch_firmware.py "C:\path\G6P_AJB_Sony_WIRE_V1.10.bin" "C:\path\G6P_AJB_SONY_V110_OLED_EXPERIMENTAL.bin"
```

Input SHA-256: `e4471c6d6cb3b50f2d39f178900d1ce4a52f6f71e53d90f5bc46123b3d090a3e`

Output SHA-256: `eabe3b903c6fc2a21df7c45e053bf89792b0c51d27a8ef518643682c676c18b3`

The tool validates the input, its CRC and header, verifies the generated hash, and refuses to overwrite an existing output. It does not access the gimbal or open a serial port.

## Installation

The successful report concerns one G6 Plus using the Windows updater and a USB-to-UART bridge. Follow the manufacturer's G6 Plus upgrade instructions, choose the **keyboard/AJB** update and the generated file, and retain the matching official firmware. The published manual specifies 115200 baud and an installed battery. The exact installed variant before the reported repair was not independently read back, and no post-flash readback was performed. If the update does not complete, avoid interrupting or attempting unrelated operations; consult the manufacturer's instructions. USB recovery after a failed flash remains unverified.

## What changed

Analysis of the recovered AJB APP found a periodic OLED sequence `40 81 AD 30`. This patch replaces one call with two Thumb NOPs, producing `40 AD 30` in a controlled emulation of that code window. It does not alter the 64-line multiplex setting. Whether the physical controller preserves command parameters across separate transactions and why the patch fixes this display remain unverified. See [technical details](docs/technical.md).

## Contributing

Please report the exact gimbal model, firmware variant, OLED markings, original symptom, update method and outcome. Never include serial numbers or private information. Do not upload proprietary firmware or updater files to issues.
