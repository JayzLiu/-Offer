class Solution(object):
    def str_to_int(self, string):
        if not string:
            return None
        neg_flag = False
        s_index = 0
        if string[0] in ['+', '-']:
            neg_flag = string[0] == '-'
            s_index += 1
        num = 0
        if not string[s_index:]:
            return None
        for i in range(s_index, len(string)):
            if ord(string[i]) < ord('0') or ord(string[i]) > ord('9'):
                return None
            num = num * 10 + ord(string[i]) - ord('0')
        if neg_flag:
            return -num
        else:
            return num

    def test(self):
        string = '+123'
        print(string, self.str_to_int(string))


s = Solution()
s.test()
