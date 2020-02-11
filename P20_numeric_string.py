class Solution(object):
    def __init__(self):
        self.index = 0

    def test(self):
        string = '+100'
        print(self.is_numeric(string))
        string = '5e2'
        print(self.is_numeric(string))
        string = '-123'
        print(self.is_numeric(string))
        string = '3.1416'
        print(self.is_numeric(string))
        string = '1E-16'
        print(self.is_numeric(string))
        string = '12e'
        print(self.is_numeric(string))
        string = '1a3.14'
        print(self.is_numeric(string))

    def is_numeric(self, string):
        # +|-N[.N][e|EN] or .N[e|EN]]
        self.index = 0
        if not string:
            return False
        numeric = self.scan_interger(string, unsigned=False) 
        if len(string) > self.index and string[self.index] == '.':
            self.index += 1
            string = string[0:]
            #1 .123
            #2 233.
            #3 233.123
            numeric = self.scan_interger(string, unsigned=True) or numeric
        if len(string) > self.index and (string[self.index] == 'e' or string[self.index] == 'E'):
            self.index += 1
            numeric = self.scan_interger(string , unsigned=False) and numeric
        return numeric and self.index == len(string)


    def scan_interger(self, string, unsigned):
        if not unsigned:
            if self.index < len(string) and (string[0] == '+' or string[0] == '-'):
                self.index += 1
        start = self.ind    ex
        while self.index < len(string) and ord(string[self.index]) >= ord('0') and ord(string[self.index]) <= ord('9'):
            self.index += 1
        return start < self.index


s = Solution()
s.test()