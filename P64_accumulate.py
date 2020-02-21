from functools import reduce
class Solution(object):
    def sum1(self, n):
        return n and n + self.sum1(n - 1)

    def __init__(self):
        self.funcs = [self.b_part, self.r_part]

    def r_part(self, n):
        return n + self.funcs[not not n - 1](n-1)

    def b_part(self, n):
        return 0

    def sum3(self, n):
        def add(x, y):
            return x + y
        return reduce(add, range(n+1))

    def test(self):
        n = 4
        print('sum1', n, self.sum1(n))
        print('sum2', n, self.funcs[not not n](n))
        print('sum3', n, self.sum3(n))


s = Solution()
s.test()