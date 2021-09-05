import unittest

def format_dec(num1: float, num2: int):
    """
        given a floating point number, set the precision
        to the desired digits after the decimal point
    """
    num = f'.{num2}f'
    return float(format(num1, num))


class TestFormatDec(unittest.TestCase):

    def test_foramt_dec(self):
        self.assertEqual(format_dec(2.09090, 2), 2.09, "should be 2.09")
        self.assertEqual(format_dec(3.1111023, 3), 3.111, "should be 3.111")
        self.assertEqual(format_dec(3.1415926536, 4), 3.1416, "should be 3.1416")
        self.assertEqual(format_dec(2.1, 2), 2.10, "should be 2.10")

if __name__ == "__main__":
    unittest.main()