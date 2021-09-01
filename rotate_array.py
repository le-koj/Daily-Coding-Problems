import unittest

def rotate_array(arr: list, k: int):
    """
    Given an array on N length, rotate the array rightwards by K rotations, i.e 
    shift each element to the right by K positions.
    """

    return arr[-k::] + arr[:(len(arr) - k)]


class TestRotateArray(unittest.TestCase):

    def test_rotate_array(self):
        self.assertEqual(rotate_array([1,2,3,4,5,6,7], 2), [6,7,1,2,3,4,5], "should be [6,7,1,2,3,4,5]")
        self.assertEqual(rotate_array([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4], "should be [5,6,7,1,2,3,4]")
        self.assertEqual(rotate_array(['john', 'jacob', 'jingle', 'hummer', 'smith'], 1), ['smith', 'john', 'jacob', 'jingle', 'hummer'], "should be ['smith', 'john', 'jacob', 'jingle', 'hummer']")


if __name__ == '__main__':
    unittest.main()

        