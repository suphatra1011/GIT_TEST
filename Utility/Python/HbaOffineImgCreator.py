#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

OFFLINE_IMAGE_SIZE = 16 * 1024 * 1024             #16 MB
FWBLOCK1_START_ADDRESS = 0x00BA0000
FWBLOCK2_START_ADDRESS = 0x00DE0000
XDATA_SIZE = 4160


def main():
    if len(sys.argv) < 3:
        print ("Usage:", sys.argv[0], "<bios file> <fw file> <output: offline image>")
        sys.exit(1)    

    bios_file = sys.argv[1]
    fw_file = sys.argv[2]
    offline_file = sys.argv[3]

    with open(offline_file, 'wb') as f:
        # 1. initial offline image 
        f.write(b'\xff' * OFFLINE_IMAGE_SIZE)

        # 2. fill bios image 
        bios_data = readfile(bios_file)
        f.seek(0)
        f.write(bios_data)

        # 3. fill fw image to block1
        fw_data = readfile(fw_file)
        xdata = list (fw_data) [-XDATA_SIZE:]
   
        f.seek(FWBLOCK1_START_ADDRESS)
        f.write(fw_data)

        # 4. fill fw image to block2 
        f.seek(FWBLOCK2_START_ADDRESS)
        f.write(fw_data)

        # 5. fill xdata
        f.seek(OFFLINE_IMAGE_SIZE - XDATA_SIZE)
        f.write(bytearray(xdata))

        f.flush()


def readfile(filename):
    return open(filename, 'rb').read()


if __name__ == "__main__":
    main()
