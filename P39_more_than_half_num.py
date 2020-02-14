class Solution(object):
    def more_than_half_num(self, array):
        if not array:
            return None
        res = None
        count = 0
        for num in array:
            if count == 0:
                res = num
                count += 1
            else:
                if num != res:
                    count -= 1
                else:
                    count += 1
        if self.is_more_than_half(array, res):
            return res
        else:
            return None

    def more_than_half_num_by_quicksort(self, array):
        if not array:
            return None
        middle = len(array) // 2
        start = 0
        end = len(array) - 1
        index = self.partition(array, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.partition(array, start, end)
            if index < middle:
                start = index + 1
                index = self.partition(array, start, end)
        res = array[index]
        if self.is_more_than_half(array, res):
            return res
        else:
            return None


    def partition(self, array, start, end):
        assert array
        small = start - 1
        for i in range(start, end):
            if array[i] < array[end]:
                small += 1
                if small != i:
                    temp = array[small]
                    array[small] = array[i]
                    array[i] = temp
        small += 1
        temp = array[small]
        array[small] = array[end]
        array[end] = temp
        return small

    def is_more_than_half(self, array, num):
        count = 0
        for item in array:
            if item == num:
                count += 1
        return count > len(array) // 2

    def test(self):
        arr = [1,2,3,2,5,2,2]
        print(arr)
        print(arr, self.more_than_half_num_by_quicksort(arr))
        arr = [1, 2, 3, 2, 5, 2, 2]
        print(arr)
        print(arr, self.more_than_half_num(arr))


s = Solution()
s.test()
