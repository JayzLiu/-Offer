class Solution(object):
    def get_the_number_of_1(self, number):
        if not number or not isinstance(number, int):
            return None
        else:
            return self.number_of_1(str(number))

    def number_of_1(self, string):
        # Time: O(log(n))
        if not string:
            return None
        num_digits = len(string)
        if num_digits == 1:
            if string[0] == '1':
                return 1
            else:
                return 0
        if string[0] == '0':
            one_in_high = 0
        elif string[0] == '1':
            one_in_high = int(string[1:]) + 1
        else:
            one_in_high = 10**(num_digits - 1)
        # 1~1345
        other_one_in_part1 = self.number_of_1(string[1:])
        # 1346~21345
        other_one_in_part2 = int(string[0]) * (num_digits-1) * 10**(num_digits-2)
        a = one_in_high + other_one_in_part1 + other_one_in_part2
        return a

    def number_of_1_quick(self, number):
        if not number or not isinstance(number, int):
            return None
        number = str(number)
        count = 0
        num_digits = len(number)
        for i in range(num_digits):
            before = int(number[:i]) if number[0:i] else 0
            behind = int(number[i+1:]) if number[i+1:] else 0
            if number[i] == '0':
                count += before * 10**(num_digits - 1 - i)
            elif number[i] == '1':
                count += before * 10**(num_digits - 1 - i) + behind + 1
            else:
                count += (1 + before) * 10**(num_digits - i - 1)
        return count


    def test(self):
        number = 100
        print(number, self.get_the_number_of_1(number))
        print(number, self.number_of_1_quick(number))


s = Solution()
s.test()
