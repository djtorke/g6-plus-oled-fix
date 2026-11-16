#!/usr/bin/env python3
"""Create the documented G6 Plus AJB Sony V1.10 OLED experiment offline."""
import argparse
import binascii
import hashlib
import pathlib
import struct

ORIGINAL = 'e4471c6d6cb3b50f2d39f178900d1ce4a52f6f71e53d90f5bc46123b3d090a3e'
RESULT = 'eabe3b903c6fc2a21df7c45e053bf89792b0c51d27a8ef518643682c676c18b3'
OFFSET = 0x2848
BEFORE = bytes.fromhex('5e3ad800ba0c9019bf3fb85cc3e40a58')
AFTER = bytes.fromhex('6590ad90624f638e3ccc6a12db6ae412')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('official', type=pathlib.Path, help='Official AJB Sony V1.10 WIRE file')
    parser.add_argument('output', type=pathlib.Path, help='New output file; must not exist')
    args = parser.parse_args()
    original = args.official.read_bytes()
    if sha(original) != ORIGINAL or len(original) != 107528:
        parser.error('Wrong input: expected the exact official AJB Sony V1.10 WIRE SHA-256 ' + ORIGINAL)
    if struct.unpack_from('<HHH', original, 2) != (105, 0, 0):
        parser.error('Unexpected page counts')
    if struct.unpack_from('<H', original)[0] != binascii.crc_hqx(original[2:], 0xffff):
        parser.error('Official file CRC mismatch')
    if original[OFFSET:OFFSET + 16] != BEFORE:
        parser.error('Unexpected original block')
    result = bytearray(original)
    result[OFFSET:OFFSET + 16] = AFTER
    struct.pack_into('<H', result, 0, binascii.crc_hqx(result[2:], 0xffff))
    if sha(result) != RESULT:
        parser.error('Generated file hash mismatch')
    with args.output.open('xb') as output:
        output.write(result)
    if sha(args.output.read_bytes()) != RESULT:
        raise RuntimeError('Written output failed SHA-256 verification')
    print('Created:', args.output)
    print('SHA-256:', RESULT)
    print('CRC16: 8BA9; pages: 105, 0, 0')


if __name__ == '__main__':
    main()
