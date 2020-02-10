class Solution(object):
    def test(self):
        test_num = 19
        print(self.count_num_of_one(test_num))
        test_num = -19
        print(self.count_num_of_one(test_num))
        test_num = 19
        print(self.count_num_of_one_v2(test_num))
        test_num = -19
        print(self.count_num_of_one_v2(test_num))


    def count_num_of_one(self, number):
        flag = 1
        count = 0
        while flag & 0xffffffff != 0:
            # print(bin(flag & 0xffffffff))
            if number & flag :
                count += 1
            flag <<= 1
        return count

    def count_num_of_one_v2(self, number):
        count = 0
        while number & 0xffffffff != 0:
            # print(bin(number & 0xffffffff))
            number &= number - 1
            count += 1
        return count


s = Solution()
s.test()