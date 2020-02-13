class Solution(object):
    def is_legal(self, sequence):
        if not sequence:
            return False
        cur_root = sequence[-1]
        len_of_seq = len(sequence)
        i = 0
        while i < len_of_seq - 1:
            if sequence[i] >= cur_root:
                break
            i += 1
        j = i
        while j < len_of_seq - 1:
            if sequence[j] <= cur_root:
                return False
            j += 1
        left_is_legal = True
        right_is_legal = True
        if i > 0:
            left_is_legal = self.is_legal(sequence[:i])
        if i < len_of_seq - 1:
            right_is_legal = self.is_legal(sequence[i:-1])
        return left_is_legal and right_is_legal


    def test(self):
        arr = [5,7,6,9,11,10,8]
        print(arr, self.is_legal(arr))
        arr = []
        print(arr, self.is_legal(arr))
        arr = [7,4,6,5]
        print(arr, self.is_legal(arr))
        

s = Solution()
s.test()
