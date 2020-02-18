class Solution(object):
    def get_the_max_sum(self, array):
        # Time: O(n)
        # Space: O(n)
        if not array:
            return None
        max_sum = array[0]
        cur_sum = array[0]
        i = 1
        while i < len(array):
            if max_sum <= 0 :
                max_sum = max(max_sum, array[i])
                cur_sum = array[i]
            else:
                cur_sum += array[i]
                max_sum = max(max_sum, cur_sum)
            i += 1
        return max_sum

    def get_the_max_sum_by_dp(self, array):
        # Time: O(n)
        # Space: O(n)
        if not array:
            return None
        sum_arr = []
        for i in range(len(array)):
            if i == 0 or sum_arr[i-1] <= 0:
                sum_arr.append(array[i])
            else:
                sum_arr.append(sum_arr[i-1] + array[i])
        return max(sum_arr)

    def test(self):
        arr = [-3, 4, -1, 6, -7, 4, 3]
        print(arr, self.get_the_max_sum(arr))
        print(arr, self.get_the_max_sum_by_dp(arr))

s = Solution()
s.test()