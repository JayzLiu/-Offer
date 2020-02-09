class Solution(object):
    def test(self):
        r_array1 = [3, 4, 5, 1, 2]
        print(self.find_minimum(r_array1))
        r_array2 = [1, 1, 1, 0, 1]
        print(self.find_minimum(r_array2))
        r_array3 = [1, 0, 1, 1, 1]
        print(self.find_minimum(r_array3))

    def find_minimum(self, r_array):
        if len(r_array) == 0:
            return None
        pre_index = 0
        post_index = len(r_array)-1
        mid_index = 0
        while r_array[pre_index] >= r_array[post_index]:
            mid_index = (pre_index + post_index) // 2
            if pre_index+1 == post_index:
                return r_array[post_index]
            if r_array[pre_index] == r_array[mid_index] and r_array[pre_index] == r_array[post_index]:
                return self.find_minumum_by_traversal(r_array[pre_index:post_index+1])
            if r_array[pre_index] >= r_array[mid_index]:
                post_index = mid_index
            else:
                pre_index = mid_index
        return r_array[mid_index]

    def find_minumum_by_traversal(self, array):
        minimum = None
        if array:
            minimum = array[0]
            for item in array:
                if item < minimum:
                    minimum = item
        return minimum

s = Solution()
s.test()