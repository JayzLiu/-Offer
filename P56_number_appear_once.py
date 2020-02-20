class Solution(object):
    def number_appear_once(self, array):
        if not array or len(array) < 2:
            return None
        xor_res = 0
        for num in array:
            xor_res ^= num
        i = 0
        while xor_res & 1 != 1 and i < 32:
            xor_res >>= 1
            i += 1
        startdard = 2 ** i
        res1 = 0
        res2 = 0
        for num in array:
            if num & startdard == 0:
                res1 ^= num
            else:
                res2 ^= num
        return res1, res2

    def one_once_other_three_times(self, array):
        if not array or len(array) < 4:
            return None
        bit_sum = [0] * 32
        for num in array:
            for i in range(32):
                bit_sum[i] += num & 1
                num >>= 1
        res = 0
        for i in reversed(range(32)):
            res <<= 1
            if bit_sum[i] % 3 == 1:
                res += 1
        if 2**31 & res:
            print(bin(res))
            res = -(~(res - 1) & 0xffffffff) 
            print(bin(res))
        return res

    def test(self):
        array = [2, -4, 3, 6, 3, 2, 5, 5]
        print(array, self.number_appear_once(array))
        array = [1, 1, 1, -2, 3, 3, 3]
        print(array, self.one_once_other_three_times(array))


s = Solution()
s.test()