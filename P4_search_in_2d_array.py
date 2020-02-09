
class Solution(object):
    # Time: O(n)
    def find(self, target, array):
        row = len(array)
        if row <= 0:
            return False
        i = 0
        column = len(array[0])
        if column <= 0:
            return False
        j = column - 1
        while i <= row-1 and j >= 0:
            reference = array[i][j]
            if reference == target:
                return True
            elif reference > target:
                j -= 1
            else:
                i += 1
        return False

    def test(self):
        target = 7
        array = [[1, 2, 8, 9],
                 [2, 4, 9, 12],
                 [4, 7, 10, 13],
                 [6, 8, 11, 15]]
        res = self.find(target, array)
        if res:
            print("Success")
        else:
            print("Failed")

s = Solution()
s.test()

