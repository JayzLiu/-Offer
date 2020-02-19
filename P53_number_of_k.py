class Solution(object):
    def number_of_k(self, array, target):
        def index_of_first(array, start, end, k):
            if start > end:
                return -1
            middle = (start + end) // 2
            if array[middle] == k:
                if middle == 0 or (middle >0 and array[middle-1] != k):
                    return middle
                else:
                    return index_of_first(array, start, middle-1, k)
            elif array[middle] > k:
                return index_of_first(array, start, middle-1, k)
            else:
                return index_of_first(array, middle+1, end, k)

        def index_of_last(array, start, end, k):
            if start > end:
                return -1
            middle = (start + end) // 2
            if array[middle] == k:
                if middle == len(array) - 1 or array[middle+1] != k:
                    return middle
                else:
                    return index_of_last(array, middle+1, end, k)
            elif array[middle] > k:
                return index_of_last(array, start, middle-1, k)
            else:
                return index_of_last(array, middle+1, end, k)

        if array == None or target == None:
            return None
        if len(array) == 0:
            return 0
        first = index_of_first(array, 0, len(array)-1, target)
        last = index_of_last(array, 0, len(array)-1, target)
        if first >= 0 and last >= 0:
            return last - first + 1
        else:
            return 0

    def missing_number(self, array):
        def mismatching_number(array, start, end):
            if start > end:
                return -1
            middle = (start + end) // 2
            if middle == array[middle]:
                return mismatching_number(array, middle+1, end)
            elif middle < array[middle]:
                if middle == 0 or array[middle-1] == middle-1:
                    return middle
                else:
                    return mismatching_number(array, start, middle-1)
            else:
                return -1
        if not array:
            return None
        return mismatching_number(array, 0, len(array)-1)

    def number_equaling_index(self, array):
        def matching_number(array, start, end):
            if start > end:
                return None
            middle = (start + end) // 2
            if middle == array[middle]:
                return middle
            elif middle > array[middle]:
                return matching_number(array, middle+1, end)
            else:
                return matching_number(array, start, middle-1)
        if not array:
            return None
        return matching_number(array, 0, len(array)-1)

    def test(self):
        array = [1,2,3,3,3,3,4,5]
        print(array, self.number_of_k(array, 3))
        array = [0,1,2,3,5,6,7]
        print(array, self.missing_number(array))
        array = [-3,-1,1,3,5]
        print(array, self.number_equaling_index(array))


s = Solution()
s.test()