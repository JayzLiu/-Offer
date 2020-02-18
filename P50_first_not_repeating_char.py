class Solution(object):
    def find(self, string):
        if not string:
            return None
        count = [0] * 256
        for char in string:
            count[ord(char)] += 1
        target = None
        for char in string:
            if count[ord(char)] == 1:
                target = char
                break
        return target

    def __init__(self):
        self.occur = [-1] * 256
        self.index = 0

    def read(self, char):
        if self.occur[ord(char)] == -1:
            self.occur[ord(char)] = self.index
        else:
            self.occur[ord(char)] = -2
        self.index += 1

    def find_for_stream(self):
        min_index = None
        for i in range(256):
            if self.occur[i] >= 0 and (min_index == None or self.occur[i] < min_index):
                min_index = self.occur[i]
                char = chr(i)
        return char, min_index

    def test(self):
        string = 'abaccdeff'
        print(string, self.find(string))
        for ch in string:
            self.read(ch)
        print(self.find_for_stream())



s = Solution()
s.test()
