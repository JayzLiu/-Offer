from functools import cmp_to_key

class Solution(object):
    def min_number(self, array):
        if not array:
            return None
        def str_cmp(a, b):
            assert isinstance(a, str) and type(a) == type(b)
            if a+b > b+a:
                return 1
            elif a+b == b+a:
                return 0
            else:
                return -1
        sorted_list = sorted(map(str, array), key=cmp_to_key(str_cmp))
        return ''.join(sorted_list)

    def test(self):
        array = [3, 32, 321]
        print(array, self.min_number(array))


s = Solution()
s.test()