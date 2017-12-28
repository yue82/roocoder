# -*- coding: utf-8 -*-


class NAL(object):
    num = 0
    def __init__(self, nal):
        self.idx = NAL.num
        NAL.num += 1
        self.ref_idc = 0
        self.unit_type = 0
        self.svc_extension_flag = 0
        self.avc_3d_extension_flag = 0
        self.rbsp = bytes()

        header = nal[0]
        if header & 0b10000000 != 0:
            assert('error: forbidden_zero_bit != 0')
        self.ref_idc = (header & 0b01100000) >> 5
        self.unit_type = header & 0b00011111
        if self.unit_type == 14 or self.unit_type == 20 or self.unit_type == 21:
            if self.unit_type != 21:
                self.svc_extension_flag = 1
            else:
                self.avc_3d_extension_flag = 1
        self.rbsp = nal[1:]

    def __str__(self):
        return '[{:>6}] IDC:{}, Unit type:{:2}, RBSP len:{}'.format(
            self.idx, self.ref_idc, self.unit_type, len(self.rbsp))


class SPS(object):
    def __init__(self, nal):
        print(nal.rbsp.hex())
        self.profile_idc = nal.rbsp[0]
        self.constraint_set_flags = nal.rbsp[1]
        self.level_idc = nal.rbsp[2]
        print(self.profile_idc, self.constraint_set_flags, self.level_idc)
