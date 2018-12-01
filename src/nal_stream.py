# -*- coding: utf-8 -*-

from NAL import *


class NALStream(object):
    def __init__(self, fp):
        self.fp = fp

    def read_one(self):
        buf = bytes()
        zero_count = 0
        while True:
            byte = self.fp.read(1)
            if byte == b'':
                return None
            if byte == b'\x00':
                zero_count += 1
            elif zero_count >= 2 and byte == b'\x01':
                if not buf == b'':
                    self.nal = self.create_nal(buf)
                    return self.nal
                zero_count = 0
            elif zero_count >= 2 and byte == b'\x03':
                continue
            else:
                buf += b'\x00' * zero_count
                zero_count = 0
                buf += byte
        if buf != b'':
            self.nal = self.create_nal(buf)
            return self.nal

    def create_nal(self, buf):
        return NAL(buf[0], buf[1:])
