import unittest

def transpose(mat: list):
    tr_matrix = [[] for i in mat[0]]

    for item in mat:
        for index in range(len(item)):
            tr_matrix[index].append(item[index])
    return tr_matrix

def is_symmetric(mat: list):
    tr = transpose(mat)

    if tr == mat:
        print('Yes')
        return 'Yes'
    else:
        print('No')
        return 'No'


class TestTranspose(unittest.TestCase):

    def test_transpose(self):
        mat1 = [[6, 4, 24, -3],
                [1, -9, 8, 0.9]]

        mat2 = [[1, 2],
                [2, 3]]

        mat3 = [[-3, 1, 0],
                [3, -3, 4],
                [7, -9, 0]]

        mat4 = [[3, 2, 4],
                [2, 0, -5],
                [4, -5, 1]]

        mat5 = [[1, 7, 3],
                [7, 4, 5],
                [3, 5, 0]]

        self.assertEqual(transpose(mat1), [[6, 1], [4, -9], [24, 8], [-3, 0.9]], "should be [[6, 6], [4, -9], [24, 8], [-3, 0.9]]")
        self.assertEqual(transpose(mat2), [[1, 2], [2, 3]], "should be [[1, 2], [2, 3]]")
        self.assertEqual(transpose(mat3), [[-3, 3, 7], [1, -3, -9], [0, 4, 0]], "should be [[-3, 3, 7], [1, -3, -9], [0, 4, 0]]")
        self.assertEqual(transpose(mat4), [[3, 2, 4], [2, 0, -5], [4, -5, 1]], "should be [[3, 2, 4], [2, 0, -5], [4, -5, 1]]")
        self.assertEqual(transpose(mat5), [[1, 7, 3], [7, 4, 5], [3, 5, 0]], "should be [[1, 7, 3], [7, 4, 5], [3, 5, 0]]")


class TestIsSymmetric(unittest.TestCase):

    def test_is_symmetric(self):
        mat1 = [[6, 4, 24, -3],
                [1, -9, 8, 0.9]]

        mat2 = [[1, 2],
                [2, 3]]

        mat3 = [[-3, 1, 0],
                [3, -3, 4],
                [7, -9, 0]]

        mat4 = [[3, 2, 4],
                [2, 0, -5],
                [4, -5, 1]]

        mat5 = [[1, 7, 3],
                [7, 4, 5],
                [3, 5, 0]]

        self.assertEqual(is_symmetric(mat1), 'No', "Should be No")
        self.assertEqual(is_symmetric(mat2), 'Yes', "should be Yes")
        self.assertEqual(is_symmetric(mat3), 'No', "should be No")
        self.assertEqual(is_symmetric(mat4), 'Yes', "should be Yes")
        self.assertEqual(is_symmetric(mat5), 'Yes', "should be Yes")




if __name__ == '__main__':
    unittest.main()
