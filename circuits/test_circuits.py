import unittest
from circuits.circuits import HALF_ADDER,FULL_ADDER, _16BITS_ADDER,INCREMENT,MUX



class TestHALF_ADDER(unittest.TestCase):
    def test_HALF_ADDER(self):
        self.assertEqual(HALF_ADDER(0, 0), [0,0])
        self.assertEqual(HALF_ADDER(0, 1), [0,1])
        self.assertEqual(HALF_ADDER(1, 0), [0,1])
        self.assertEqual(HALF_ADDER(1, 1), [1,0])



class TestFULL_ADDER(unittest.TestCase):
    def test_FULL_ADDER(self):
        self.assertEqual(FULL_ADDER(0, 0, 0), [0,0])
        self.assertEqual(FULL_ADDER(0, 0, 1), [0,1])
        self.assertEqual(FULL_ADDER(0, 1, 0), [0,1])
        self.assertEqual(FULL_ADDER(0, 1, 1), [1,0])
        self.assertEqual(FULL_ADDER(1, 0, 0), [0,1])
        self.assertEqual(FULL_ADDER(1, 0, 1), [1,0])
        self.assertEqual(FULL_ADDER(1, 1, 0), [1,0])
        self.assertEqual(FULL_ADDER(1, 1, 1), [1,1])

class TestMUX(unittest.TestCase):
    def test_MUX(self):
        self.assertEqual(MUX(0, 0, 0), 0)
        self.assertEqual(MUX(0, 1, 0), 0)
        self.assertEqual(MUX(0, 0, 1), 1)
        self.assertEqual(MUX(0, 1, 1), 1)
        self.assertEqual(MUX(1, 0, 0), 0)
        self.assertEqual(MUX(1, 0, 1), 0)
        self.assertEqual(MUX(1, 1, 0), 1)
        self.assertEqual(MUX(1, 1, 1), 1)


class TestADD16Bit(unittest.TestCase):
    def test_all_zero(self):
        A = [0]*16
        B = [0]*16
        self.assertEqual(_16BITS_ADDER(A, B), [0]*16)

    def test_simple_add(self):
        A = [1]+[0]*15  # 1
        B = [1]+[0]*15  # 1
        self.assertEqual(_16BITS_ADDER(A, B), [0, 1]+[0]*14)  # 2

    def test_max_plus_zero(self):
        A = [1]*16  # 65535
        B = [0]*16
        self.assertEqual(_16BITS_ADDER(A, B), [1]*16)

    def test_max_plus_one(self):
        A = [1]*16  # 65535
        B = [1] + [0]*15  # 1
        self.assertEqual(_16BITS_ADDER(A, B), [0]*16)  # overflow: 65536 -> 0 (16-bit truncation)

    def test_carry_ripples(self):
        A = [1]*8 + [0]*8  # 0x00FF
        B = [1]*8 + [0]*8  # 0x00FF
        self.assertEqual(_16BITS_ADDER(A, B), [0] + [1]*8 + [0]*7)  # 255 + 255 = 510

    def test_alternating_bits(self):
        A = [1, 0]*8  # 0b01010101...
        B = [0, 1]*8  # 0b10101010...
        self.assertEqual(_16BITS_ADDER(A, B), [1]*16)  # all positions sum to 1

    def test_add_32768_and_1(self):
        A = [0]*15 + [1]  # 0x8000 (32768)
        B = [1] + [0]*15  # 0x0001 (1)
        self.assertEqual(_16BITS_ADDER(A, B), [1] + [0]*14 + [1])  # 32769

    def test_random_example(self):
        A = [1,0,1,1,0,0,1,0,  0,1,0,1,1,1,0,1]
        B = [0,1,1,0,1,1,0,1,  1,0,1,0,0,0,1,0]
        # You can use a helper function to compute expected result in Python if needed
        expected_sum = bin((int("".join(map(str, A[::-1])), 2) + int("".join(map(str, B[::-1])), 2)) & 0xFFFF)[2:].zfill(16)
        expected_sum_list = [int(bit) for bit in expected_sum[::-1]]
        self.assertEqual(_16BITS_ADDER(A, B), expected_sum_list)

class TestIncrementFunction(unittest.TestCase):
    def test_increment_all_zeros(self):
        # Test incrementing a 16-bit number with all zeros
        input_arr = [0] * 16
        expected_output = [1]+[0] * 15  # Incrementing 0 results in 1
        self.assertEqual(INCREMENT(input_arr), expected_output)

    def test_increment_no_carry(self):
        # Test incrementing a 16-bit number with no carry
        input_arr = [0] * 15 + [1]  # Binary: 1000...0000
        expected_output = [1]+[0] * 14 + [1]  # Binary: 1000...001
        self.assertEqual(INCREMENT(input_arr), expected_output)

    def test_increment_with_carry(self):
        # Test incrementing a 16-bit number with carry
        input_arr =  [1, 1] +[0]*14 # Binary: 0000...0011
        expected_output =  [0, 0, 1] + [0]*13  # Binary: 0000...0100
        self.assertEqual(INCREMENT(input_arr), expected_output)

    def test_increment_all_ones(self):
        # Test incrementing a 16-bit number with all ones (overflow)
        input_arr = [1] * 16  # Binary: 1111...1111
        expected_output = [0] * 16  # Binary: 0000...0000 (overflow)
        self.assertEqual(INCREMENT(input_arr), expected_output)


if __name__ == '__main__':
    unittest.main()
