class Solution(object):
    def test(self):
        matrix = [['a', 'b', 't', 'g'],
                  ['c', 'f', 'c', 's'],
                  ['j', 'd', 'e', 'h']]
        target_str = 'bfce'
        res = self.has_path(matrix, target_str)
        if res:
            print('Found!')

    def has_path(self, matrix, target_str):
        if not matrix or not target_str:
            return False
        visited_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res = self.has_path_core(matrix, visited_matrix, row, col, target_str)
                if res:
                    return True

    def has_path_core(self, c_matrix, v_matrix, row, col, left_str):
        if row < 0 or row >= len(c_matrix) or col < 0 or col >= len(c_matrix[0]):
            return False
        if (not v_matrix[row][col]) and c_matrix[row][col] == left_str[0]:
            if len(left_str) == 1:
                return True
            else:
                v_matrix[row][col] = 1
                if self.has_path_core(c_matrix, v_matrix, row-1, col, left_str[1:]) \
                  or self.has_path_core(c_matrix, v_matrix, row, col-1, left_str[1:]) \
                  or self.has_path_core(c_matrix, v_matrix, row+1, col, left_str[1:]) \
                  or self.has_path_core(c_matrix, v_matrix, row, col+1, left_str[1:]):
                    return True
                else:
                    v_matrix[row][col] = 0
                    return False
        else:
            return False



s = Solution()
s.test()