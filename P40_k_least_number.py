import heapq

class Solution(object):
    def get_k_least(self, array, k):
        if array == None or len(array) < k:
            return array
        start = 0
        end = len(array) - 1
        index = self.partition(array, start, end)
        while index != k - 1:
            if index < k - 1:
                start = index + 1
            if index > k - 1:
                end = index - 1
            index = self.partition(array, start, end)
        return array[:k]

    def partition(self, array, start, end):
        assert array and start >= 0 and end <= len(array)-1
        small = start - 1
        for i in range(start, end):
            if array[i] < array[end]:
                small += 1
                if i != small:
                    temp = array[small]
                    array[small] = array[i]
                    array[i] = temp
        small += 1
        temp = array[small]
        array[small] = array[end]
        array[end] = temp
        return small

    def get_k_least_by_heapq(self, array, k):
        if array == None or len(array) < k:
            return array
        heap = []
        for item in array:
            heapq.heappush(heap, item)
        return [heapq.heappop(heap) for i in range(k)]


    def test(self):
        array = [1, 7, 4, 2, 5, 3, 6]
        print(array)
        print(array, self.get_k_least(array, 4))
        array = [1, 7, 4, 2, 5, 3, 6]
        print(array)
        print(array, self.get_k_least_by_heapq(array, 4))


s = Solution()
s.test()