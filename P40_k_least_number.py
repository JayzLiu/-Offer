import heapq

class Solution(object):
    def __init__(self):
        self.heap = []

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
                    array[small], array[i] = array[i], array[small]
        small += 1
        array[small], array[end] = array[end], array[small]
        return small

    def get_k_least_by_heapq(self, array, k):
        if array == None or len(array) < k:
            return array
        for item in array:
            if len(self.heap) < k:
                heapq.heappush(self.heap, -item)
            else:
                if -self.heap[0] > item:
                    heapq.heappushpop(self.heap, -item)
        k_least = [-heapq.heappop(self.heap) for i in range(len(self.heap))]
        k_least.reverse()
        return k_least


    def test(self):
        array = [1, 7, 4, 2, 5, 3, 6]
        print(array)
        print(array, self.get_k_least(array, 4))
        array = [1, 7, 4, 2, 5, 3, 6]
        print(array)
        print(array, self.get_k_least_by_heapq(array, 4))


s = Solution()
s.test()