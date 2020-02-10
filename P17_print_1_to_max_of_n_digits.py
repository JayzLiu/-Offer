class Solution(object):
    def test(self):
        n = 4
        self.print_1_to_max_of_n_digits(n)

    def print_1_to_max_of_n_digits(self, n):
        assert isinstance(n, int)
        if n == 0:
            return
        number = [0] * n
        self.print_permutation(number, 0)

    def print_permutation(self, number, index):
        if index == len(number):
            # index exceeds (n-1)
            self.print_array(number)
        else:
            for i in range(10):
                number[index] = str(i)
                self.print_permutation(number, index+1)

    def print_array(self, number):
        for i in range(len(number)):
            if number[i] != '0':
                break
        if i == len(number) - 1 and number[i] == '0':
            return
        else:
            print(''.join(number[i:]))


s = Solution()
s.test()

