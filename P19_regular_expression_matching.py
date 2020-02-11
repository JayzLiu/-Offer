class Solution(object):
    def test(self):
        string = 'abcd'
        pattern = 'aba*c.'
        if self.re_match(string, pattern):
            print("matched!")
        else:
            print("Failed...")

    def re_match(self, string, pattern):
        if len(string) == 0 and len(pattern) > 0:
            return False
        if len(pattern) == 0:
            return len(string) == 0
        else:
            if len(pattern) >= 2 and pattern[1] == '*':
                if string[0] == pattern[0]:
                    # match the blank or one char or more than one char
                    return self.re_match(string, pattern[2:]) or self.re_match(string[1:], pattern[2:]) or self.re_match(string[1:], pattern)
                else:
                    # Use the * mode to skip
                    return self.re_match(string, pattern[2:])
            elif pattern[0] == '.' or string[0] == pattern[0]:
                return self.re_match(string[1:], pattern[1:])
            else:
                return False


s = Solution()
s.test()