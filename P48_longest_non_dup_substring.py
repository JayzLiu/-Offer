class Solution(object):
    def get_longest_len(self, string):
        if not string:
            return None
        chars = dict()
        longest = [0] * len(string)
        chars[string[0]] = 0
        max_longest = longest[0] = 1
        for i in range(1, len(string)):
            if string[i] not in chars:
                longest[i] = longest[i-1] + 1
            else:
                dist = i - chars[string[i]]
                if dist <= longest[i-1]:
                    longest[i] = dist
                else:
                    longest[i] = longest[i-1] + 1
            chars[string[i]] = i
            if max_longest < longest[i]:
                max_longest = longest[i]
        return max_longest

    def test(self):
        string = 'arabcacfr'
        print(string, self.get_longest_len(string))


s = Solution()
s.test()
