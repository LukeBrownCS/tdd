import unittest
from roman import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_I_returns_1(self):
        self.assertEqual(roman_to_int('I'), 1)
    
    def test_V_returns_5(self):
        self.assertEqual(roman_to_int('V'), 5)

if __name__ == '__main__':
    unittest.main()
