class Solution(object):
    def test(self):
        base = 2
        exponent = 6
        res = self.power(base, exponent)
        print(res)
        print(self.power(0, 1))
        print(self.power(1, 0))
        print(self.power(-1, 0))
        print(self.power(0, 0))
        print(self.power(0, -1))

    def power(self, base, exponent):
        if base == 0 and exponent < 0:
            raise Exception("Illegal input!")
        if exponent < 0:
            exponent = -exponent
        res = self.pos_power(base, exponent)
        if exponent < 0:
            res = 1 / res
        return res

    def pos_power(self, base, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.pos_power(base, exponent >> 1)
        res *= res
        if exponent & 1:
            res *= base
        return res


s = Solution()
s.test()