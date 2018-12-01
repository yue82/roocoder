# -*- coding: utf-8 -*-


import sys
sys.path.append('./src')

from nal_stream import NALStream


def main():
    in_file_name = './data/cif/bus_cif.h264'
    with open(in_file_name, 'rb') as fi:
        nals = NALStream(fi)
        while nals.read_one():
            print(nals.nal)

if __name__ == '__main__':
    main()
