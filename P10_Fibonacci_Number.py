class Solution(object):
    def calculate_Fibonacci_by_recurence(self, n):
        assert n >= 0 and isinstance(n, int)
        if n == 0 or n == 1:
            return n
        else:
            return self.calculate_Fibonacci_by_recurence(n-1)+self.calculate_Fibonacci_by_recurence(n-2)

    def calculate_Fibonacci_by_loop(self, n):
        assert n >= 0 and isinstance(n, int)
        if n <= 1:
            return n
        f_n_minus_2 = 0
        f_n_minus_1 = 1
        for i in range(2, n+1):
            f_i = f_n_minus_1 + f_n_minus_2
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = f_i
        return f_i

    def test(self):
        n = 5
        print(self.calculate_Fibonacci_by_recurence(n))
        print(self.calculate_Fibonacci_by_loop(n))

s = Solution()
s.test()