# -*- coding: utf-8 -*-

class CodeReader(object):
    def __init__(self, data):
        self.data = data
        self.byte_ptr = 0
        self.bit_ptr = 0

        def read_bits(self, n):
            ret = 0
            if not n > 0:
                return ret
            if self.bit_ptr < 8:
                byte = self.data[self.byte_ptr]
                if n > self.bit_ptr:
                    l = self.bit_ptr
                    self.bit_ptr = 8
                    return (ret << l) | (byte >> (8 - l))
                else:
                    l = n - self.bit_ptr
                    self.bit_ptr = l
                    return (ret << l) | (byte >> (8 - l))
            while n > 8:
                byte = self.data[self.byte_ptr]
                ret = ret << 8 | byte
                self.byte_ptr += 1
                n -= 8
            if n > 0:
                byte = self.data[self.byte_ptr]
                self.bit_ptr = 8 - n
                ret = (ret << n) | (byte >> (8 - n))

        def f(self, n):
            """
            f(n): fixed-pattern bit string using n bits written (from left to right) with the left bit first.
            """
            pass

        def u(self, n):
            """
            u(n): unsigned integer using n bits.
            When n is "v" in the syntax table, the number of bits varies in a manner dependent on the value of other syntax elements.
            """
            pass

        def ae(v):
            """
            # ae(v): context-adaptive arithmetic entropy-coded syntax element
            # The parsing process for this descriptor is specified in clause9.3
            """
            pass

        def b():
            """
            # b(8): byte having any pattern of bit string (8bits)
            # The parsing process for this descriptor is specified by the return value of the function read_bits(8).
            """
            pass

        def ce(v):
            """
            # ce(v): context-adaptive variable-length entropy-coded syntax element with the left bit first
            # The parsing process for this descriptor is specified in clause9.2.
            """
            pass

        def i(n):
            """
            # i(n): signed integer using n bits.When n is "v" in the syntax table, the number of bits varies in a manner dependent on the value of other syntax elements
            # The parsing process for this descriptor is specified by the return value of the function read_bits(n) interpreted as a two's complement integer representation with most significant bit written first.
            """
            pass

        def me(v):
            """
            # me(v): mapped Exp-Golomb-coded syntax element with the left bit first
            # The parsing process for this descriptor is specified in clause9.1.
            """
            pass

        def se(v):
            """
            # se(v): signed integer Exp-Golomb-coded syntax element with the left bit first
            # The parsing process for this descriptor is specified in clause9.1.
            """
            pass

        def te(v):
            """
            # te(v): truncated Exp-Golomb-coded syntax element with left bit first.The parsing process for this descriptor is specified in clause9.1.
            """
            pass

        def ue(v):
            """
            # ue(v): unsigned integer Exp-Golomb-coded syntax element with the left bit first.
            # The parsing process for this descriptor is specified in clause9.1
            """
            pass
