# -*- coding: utf-8 -*-


class NAL(object):
    num = 0
    def __new__(cls, header, rbsp):
        if header & 0b10000000 != 0:
            assert('error: forbidden_zero_bit != 0')
        unit_type = header & 0b00011111
        if unit_type == 7:
            return super().__new__(SPS)
        else:
            return super().__new__(cls)

    def __init__(self, header, rbsp):
        self.idx = NAL.num
        NAL.num += 1
        self.ref_idc = NAL.get_ref_idc(header)
        self.unit_type = NAL.get_unit_type(header)
        self.unit_type_name = ''
        self.rbsp = rbsp
        if self.unit_type == 14 or self.unit_type == 20 or self.unit_type == 21:
            if self.unit_type != 21:
                self.svc_extension_flag = 1
            else:
                self.avc_3d_extension_flag = 1

    @classmethod
    def get_unit_type(cls, header):
        return header & 0b00011111

    @classmethod
    def get_ref_idc(cls, header):
        return (header & 0b01100000) >> 5

    def __str__(self):
        return '[{:>6}] IDC:{}, Unit type:{:>4}({:2}), RBSP len:{}'.format(
            self.idx, self.ref_idc, self.unit_type_name, self.unit_type, len(self.rbsp))


class SPS(NAL):
    def __init__(self, header, rbsp):
        nal = super().__init__(header, rbsp)
        self.unit_type_name = 'SPS'
        self.profile_idc = self.rbsp[0]
        self.constraint_set_flags = self.rbsp[1]
        self.level_idc = self.rbsp[2]
