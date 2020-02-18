class Solution(object):
    def max_value(self, matrix):
        # Time: O(n^2)
        # Space: O(n)
        if not matrix or not matrix[0]:
            return None
        val_arr= [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                left = 0
                up = 0
                if i > 0:
                    up = val_arr[j]
                if j > 0:
                    left = val_arr[j-1]
                val_arr[j] = max(left, up) + matrix[i][j]
        max_value = val_arr[-1]
        return max_value

    def test(self):
        chess_board = [[1,10,3,8],
                       [12,2,9,6],
                       [5,7,4,11],
                       [3,7,16,5]]
        print(self.max_value(chess_board))

s = Solution()
s.test()