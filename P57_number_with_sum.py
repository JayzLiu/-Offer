class Solution(object):
    def two_number(self, array, sum):
        if not array or not isinstance(sum, int):
            return None
        ahead = 0
        behind = len(array) - 1
        while ahead < behind:
            cur_sum = array[ahead] + array[behind]
            if cur_sum == sum:
                return array[ahead], array[behind]
            elif cur_sum < sum:
                ahead += 1
            else:
                behind -= 1
        return None
    
    def sequential_number(self, sum):
        if not isinstance(sum, int):
            return None
        small = 1
        big = 2
        res = []
        while small <= sum // 2:
            cur_sum = (big + small) * (big - small + 1) / 2
            if cur_sum == sum:
                res.append(list(range(small, big + 1)))
                small += 1
            elif cur_sum < sum:
                big += 1
            else:
                small += 1
        if res:
            return res
        else:
            return None
    
    def test(self):
        array = [1,2,4,7,11,15]
        sum = 15
        print(array, sum, self.two_number(array, sum))
        print(sum, self.sequential_number(sum))


s = Solution()
s.test()