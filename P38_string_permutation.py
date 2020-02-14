class Solution(object):
    def __init__(self):
        self.cur_pmt = []
        self.permutation = []

    def permutate(self, string):
        def permutate_core(string):
            if not string:
                return
            if len(string) == 1:
                self.cur_pmt.append(string[0])            
                self.permutation.append(''.join(self.cur_pmt[:]))
                self.cur_pmt.pop()
                return
            for i in range(len(string)):
                self.cur_pmt.append(string[i])
                temp = string[0]
                string[0] = string[i]
                string[i] = temp
                permutate_core(string[1:])
                self.cur_pmt.pop()
            return
        self.cur_pmt = []
        self.permutation = []
        permutate_core(list(string))
        return self.permutation

    def test(self):
        string = "abc"
        print(self.permutate(string))
        


s = Solution()
s.test()
        

                