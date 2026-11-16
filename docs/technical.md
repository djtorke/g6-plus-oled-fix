# Technical evidence

The official AJB Sony V1.10 WIRE container is 107,528 bytes: CRC16/CCITT-FALSE over bytes 2 onward, then three little-endian page counts `[105, 0, 0]`, then 105 × 1024 payload bytes. The generated file has CRC `8BA9`.

The analyzed APP has SHA-256 `018b7336ec6d7fe700733f5e6c43195d34fde23e896e9c93bb7c896f3b2f227c`. Its bytes at file offset `0x2844` (candidate address `0x08007844`) change from `05 f0 61 f9` to `00 bf 00 bf`. In isolated emulation with the OLED send function intercepted, the periodic commands change from `40 81 AD 30` to `40 AD 30`. The full image is not emulated and the controller's treatment of separated transactions is unknown.

The original WIRE payload was independently reproduced from the APP by zero-padding to 105 KiB and applying AES-256-ECB using the updater's implementation. This patch replaces only the corresponding ciphertext block at file offset `0x2848` and recomputes the CRC. The generated file decrypts to the expected modified APP plus padding; the generator validates the complete SHA-256 of the input and output. The patch does not establish the installed device's actual firmware or processor attribution.

The owner reports the patched file fixed the replacement display. The number of tested devices is one. OLED controller identity, causal mechanism, recovery after interrupted update, other firmware variants and long-term behavior remain open.

References: [SSD1315 datasheet](https://dl.espressif.com/dl/schematics/SSD1315.pdf), [HP7240-01 panel specification](https://www.icbanq.com/icdownload/data/ICBShop/Board/HP7240-01-TSWG16P042-A-VER1.0.pdf), [FeiyuTech downloads](https://www.feiyu-tech.com/g6-plus/down.html).
