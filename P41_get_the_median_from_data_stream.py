from heapq import *


class Solution(object):
    def __init__(self):
        self.max_heap = [] # store opposite number due to the function of heapq
        self.min_heap = []
    
    def insert_num(self, num):
        # Time: O(log(n))
        assert num and type(num) in (int, float)
        if len(self.max_heap) + len(self.min_heap) == 0:
            heappush(self.min_heap, num)
        elif (len(self.max_heap) + len(self.min_heap)) & 1 == 0:
            if self.max_heap[0] > num:
                heappush(self.max_heap, -num)
                num = heappop(self.max_heap)
            heappush(self.min_heap, num)
        else:
            if self.min_heap[0] < num:
                heappush(self.min_heap, num)
                num = heappop(self.min_heap)
            heappush(self.max_heap, -num)
    
    def get_the_median(self):
        # Time: O(1)
        if len(self.max_heap) + len(self.min_heap) == 0:
            return None
        elif len(self.max_heap) + len(self.min_heap) & 1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0] / 2)

    def test(self):
        arr = [1,3,5,2,4,6]
        for num in arr:
            self.insert_num(num)
            print(num, self.get_the_median())


s = Solution()
s.test()
