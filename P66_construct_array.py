class Solution(object):
    def construct(self, array):
        if not array or len(array) <= 1:
            return None
        c_array = [ 1 ] * len(array)
        for i in range(1, len(c_array)):
            c_array[i] = c_array[i - 1] * array[i - 1]
        base = 1
        for i in reversed(range(len(c_array) - 1)):
            base *= array[i + 1]
            c_array[i] *= base
        return c_array

    def test(self):
        array = [1,2,3,4]
        print(array, self.construct(array))

    
s = Solution()
s.test()
            