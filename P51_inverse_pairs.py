class Solution(object):
    def inverse_pairs(self, array):
        # Time: O(nlog(n))
        # Space: O(n)
        def count_pairs(data, copy, start, end):
            assert len(data) == len(copy)
            if start == end:
                copy[start] = data[start]
                return 0
            middle = (start + end) // 2
            right = count_pairs(copy, data, middle+1, end)
            left = count_pairs(copy, data, start, middle)
            i = middle
            j = end
            copy_index = end
            count = 0
            while i >= start and j >= middle + 1:
                if data[i] > data[j]:
                    copy[copy_index] = data[i]
                    count += j - middle
                    i -= 1
                    copy_index -= 1
                else:
                    copy[copy_index] = data[j]
                    j -= 1
                    copy_index -= 1
            while i >= start:
                copy[copy_index] = data[i]
                copy_index -= 1
                i -= 1
            while j >= middle + 1:
                copy[copy_index] = data[j]
                copy_index -= 1
                j -= 1
            return left + right + count

        if not array:
            return None
        copy = [num for num in array]
        count = count_pairs(array, copy, 0, len(array)-1)
        return count

    def test(self):
        array = [7,5,6,4]
        print(array, self.inverse_pairs(array))


s = Solution()
s.test()