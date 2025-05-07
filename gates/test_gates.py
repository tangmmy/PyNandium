import unittest
from gates.gates import NAND,AND,NOT,XOR,OR



class TestNand(unittest.TestCase):
    def test_nand(self):
        self.assertEqual(NAND(0, 0), 1)
        self.assertEqual(NAND(0, 1), 1)
        self.assertEqual(NAND(1, 0), 1)
        self.assertEqual(NAND(1, 1), 0)

class TestAnd(unittest.TestCase):
    def test_And(self):
        self.assertEqual(AND(0, 0), 0)
        self.assertEqual(AND(0, 1), 0)
        self.assertEqual(AND(1, 0), 0)
        self.assertEqual(AND(1, 1), 1)

class TestNot(unittest.TestCase):
    def test_not(self):
        self.assertEqual(NOT(0), 1)
        self.assertEqual(NOT(1), 0)

class TestOr(unittest.TestCase):
    def test_or(self):
        self.assertEqual(OR(0, 0), 0)
        self.assertEqual(OR(0, 1), 1)
        self.assertEqual(OR(1, 0), 1)
        self.assertEqual(OR(1, 1), 1)

class TestXor(unittest.TestCase):
    def test_xor(self):
        self.assertEqual(XOR(0, 0), 0)
        self.assertEqual(XOR(0, 1), 1)
        self.assertEqual(XOR(1, 0), 1)
        self.assertEqual(XOR(1, 1), 0)


if __name__ == '__main__':
    unittest.main()
