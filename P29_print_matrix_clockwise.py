import copy

class Solution(object):
    def print_martix(self, matrix):
        if not matrix:
            return
        elif not matrix[0]:
            return
        matrix = copy.deepcopy(matrix)
        arr_to_print = []
        while matrix:
            arr_to_print += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        print(arr_to_print)

    def test(self):
        test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.print_martix(test_matrix)

s = Solution()
s.test()
