class Solution(object):
    def test(self):
        array = [1, 2, 3, 4, 5]
        print(self.reorder_odd_and_even(array))


    def reorder_odd_and_even(self, array):
        return self.reorder_array(array, self.is_odd)

    def reorder_array(self, array, func):
        if not array:
            return array
        begin_index = 0
        end_index = len(array)-1
        while begin_index < end_index:
            while begin_index < end_index and not func(array[begin_index]):
                begin_index += 1
            while end_index > 0 and func(array[end_index]):
                end_index -= 1
            if begin_index < end_index:
                temp = array[begin_index]
                array[begin_index] = array[end_index]
                array[end_index] = temp
        return array

    def is_odd(self, num):
        return num % 2 == 0


s = Solution()
s.test()