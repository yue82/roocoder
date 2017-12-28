# -*- coding: utf-8 -*-


import sys
sys.path.append('./src')

from NAL import *


def main():
    in_file_name = 'data/cif/bus_cif.h264'

    nals = []
    with open(in_file_name, 'rb') as fi:
        zero_count = 0
        buf = bytes()

        while True:
            byte = fi.read(1)
            if byte == b'':
                break

            if byte == b'\x00':
                zero_count += 1
            elif zero_count >= 2 and byte == b'\x01':
                if not buf == b'':
                    nals.append(NAL(buf))
                    buf = b''
                zero_count = 0
            elif zero_count >= 2 and byte == b'\x03':
                continue
            else:
                buf += b'\x00' * zero_count
                zero_count = 0
                buf += byte
        if not buf == b'':
            nals.append(NAL(buf))

        for nal in nals:
            print(nal)
            if nal.unit_type == 7:
                SPS(nal)
        # print('\n'.join([str(nal) for nal in nals]))


if __name__ == '__main__':
    main()
