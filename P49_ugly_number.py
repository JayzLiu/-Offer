class Solution(object):
    def get_the_n_ugly_number(self, n):
        if type(n) != int or n <= 0:
            return None
        ugly_nums = [1]
        index = 1
        f2_i = 0
        f3_i = 0
        f5_i = 0
        while index < n:
            cur_num = min(ugly_nums[f2_i]*2, ugly_nums[f3_i]*3, ugly_nums[f5_i]*5)
            ugly_nums.append(cur_num)
            if ugly_nums[f2_i] * 2 == ugly_nums[index]:
                f2_i += 1
            if ugly_nums[f3_i] * 3 == ugly_nums[index]:
                f3_i += 1
            if ugly_nums[f5_i] * 5 == ugly_nums[index]:
                f5_i += 1
            index += 1
        return ugly_nums[-1]

    def test(self):
        index = 10
        print(index, self.get_the_n_ugly_number(index))


s = Solution()
s.test()
