class Solution(object):
    def maximal_profit(self, array):
        if not array or len(array) <= 2:
            return None
        lowest = array[0]
        max_diff = array[1] - array[0]
        for i in range(1, len(array)):
            if array[i] - lowest > max_diff:
                max_diff = array[i] - lowest
            if array[i] < lowest:
                lowest = array[i]
        return max_diff
    
    def test(self):
        prices = [9,11,8,5,7,12,16,14]
        print(prices, self.maximal_profit(prices))


s = Solution()
s.test()