class Solution(object):
    def test(self):
        pass

    def moving_count(self, matrix, k):
        if not (matrix and matrix[0]):
            return None
        viewed_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]
        res = self.DFS(matrix, viewed_matrix, 0, 0, k)
        return res

    def DFS(self, m_matrix, v_matrix, row, col, k):
        assert m_matrix and m_matrix[0]
        count = 0
        if row < 0 or row >= len(m_matrix) or col < 0 or col >= len(m_matrix[0]) or v_matrix[row][col] == 1:
            return count
        else:
            if self.check_sum(row, col, k):
                v_matrix[row][col] = 1
                count = 1 + self.DFS(m_matrix, v_matrix, row - 1, col, k) \
                        + self.DFS(m_matrix, v_matrix, row, col - 1, k) \
                        + self.DFS(m_matrix, v_matrix, row + 1, col, k) \
                        + self.DFS(m_matrix, v_matrix, row, col + 1, k)
            return count

    def check_sum(self, row, col, k):
            sum = 0
            while row > 0:
                sum += row % 10
                row //= 10
            while col > 0:
                sum += col % 10
                col //= 10
            return sum