'''
找出数组中重复的数字：长度为n的数组范围在0~n-1之间
'''


class Solution1(object):
    # Time: O(nlogn)
    # Space: O(1)
    def find_duplicated_num_1(self, nums, dup_num):
        len_of_nums = len(nums)

        if len_of_nums <= 1:
            return False
        for num in nums:
            if num < 0 or num > len_of_nums - 1:
                return False

        nums.sort()
        pre = nums[0]
        for i in range(1, len_of_nums):
            cur = nums[i]
            if pre == cur:
                dup_num[0] = cur
                return True
            pre = cur
        return False

    # Time: O(n)
    # Space: O(n)
    def find_duplicated_num_2(self, nums, dup_num):
        len_of_nums = len(nums)

        if len_of_nums <= 1:
            return False
        for num in nums:
            if num < 0 or num > len_of_nums - 1:
                return False

        num_set = set()
        for num in nums:
            if num in num_set:
                dup_num[0] = num
                return True
            else:
                num_set.add(num)
        return False

    # Time: O(n)
    # Space: O(1)
    def find_duplicated_num(self, nums, dup_num):
        len_of_nums = len(nums)

        if len_of_nums <= 1:
            return False
        for num in nums:
            if num < 0 or num > len_of_nums - 1:
                return False

        for i in range(len_of_nums):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    dup_num[0] = nums[i]
                    return True
                else:
                    temp = nums[i]
                    nums[i] = nums[temp]
                    nums[temp] = temp

        return False

    def test(self):
        nums = [2, 3, 1, 0, 2, 5, 3]
        dup_num = [-1]
        res = self.find_duplicated_num(nums, dup_num)
        if res:
            print(dup_num[0])


'''
不修改数组找出重复的数字：长度为n的数组范围在1~n+1之间（必有重复）
'''


class Solution2(object):
    # Time: O(nlogn)
    # Space: O(1)
    def find_duplicated_num(self, nums, dup_num):
        len_of_nums = len(nums)

        if len_of_nums <= 1:
            return False
        for num in nums:
            if num < 0 or num > len_of_nums - 1:
                return False

        start = 1
        end = len_of_nums - 1
        while start < end:
            middle = (end + start) // 2
            count_in_range = self.count_for_specified_range(nums, start, middle)
            if count_in_range > middle - start + 1:
                end = middle
            else:
                start = middle + 1
        if count_in_range > 1:
            dup_num[0] = start
            return True
        else:
            return False

    def count_for_specified_range(self, nums, start, end):
        count = 0
        for num in nums:
            if num >= start and num <= end:
                count += 1
        return count

    def test(self):
        nums = [2, 3, 5, 4, 3, 2, 6, 7]
        dup_num = [-1]
        res = self.find_duplicated_num(nums, dup_num)
        if res:
            print(dup_num[0])


if __name__ == "__main__":
    s = Solution2()
    s.test()
