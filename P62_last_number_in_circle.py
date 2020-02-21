class Solution(object):
    def last_number(self, n, m):
        # Space: O(n)
        # Time: O(nm)
        if not isinstance(n, int) or not isinstance(m, int) or abs(m)*n <= 0 :
            return None
        array = [i for i in range(n)]
        real_i = -1
        while len(array) > 1:
            i = 0
            while i < m:
                if real_i == len(array) - 1:
                    real_i = 0
                else:
                    real_i += 1
                i += 1
            array.pop(real_i)
            real_i -= 1
        return array[0]

    def last_number_by_recurence(self, n, m):
        # Space: O(1)
        # Time: O(n)
        if not isinstance(n,int) or not isinstance(m, int) or abs(m) * n <= 0:
            return None
        cur_res = 0
        for i in range(1, n + 1):
            cur_res = (cur_res + m) % i
        return cur_res

    def test(self):
        n = 5
        m = 3
        print(n, m, self.last_number(n, m))
        print(n, m, self.last_number_by_recurence(n, m))


s = Solution()
s.test()
