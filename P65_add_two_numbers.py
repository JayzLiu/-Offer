class Solution(object):
    def add(self, x , y):
        sum = x ^ y
        carry = (x & y) << 1
        while carry:
            sum, carry = (sum ^ carry) & 0xffffffff, ((sum & carry) << 1) & 0xffffffff
            # print(bin(sum))
            # print(bin(carry))
            # print(sum, carry)
        return sum if sum <= 0x7fffffff else -((~sum + 1) & 0xffffffff)

    def test(self):
        x = -1
        y = -6
        print(x, y, self.add(x, y))

s = Solution()
s.test()
