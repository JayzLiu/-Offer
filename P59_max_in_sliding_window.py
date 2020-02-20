class Solution(object):
    def max_in_sliding(self, array, window_size):
        if not array or not window_size or len(array) < window_size:
            return None
        bqueue = []
        for i in range(window_size - 1):
            while bqueue and array[bqueue[-1]] <= array[i]:
                bqueue.pop()
            bqueue.append(i)
        max_list = []
        for i in range(window_size - 1, len(array)):
            if i - bqueue[0] >= window_size:
                bqueue.pop(0)
            while bqueue and array[bqueue[-1]] <= array[i]:
                bqueue.pop()
            bqueue.append(i)
            max_list.append(array[bqueue[0]])
        return max_list

    def __init__(self):
        self.queue = []
        self.max_queue = []

    def push_back(self, item):
        while self.max_queue and self.max_queue[-1] <= item:
            self.max_queue.pop()
        self.max_queue.append(item)
        self.queue.append(item)
    
    def pop_front(self):
        if self.queue[0] == self.max_queue[0]:
            self.max_queue.pop(0)
        return self.queue.pop(0)

    def max(self):
        if self.max_queue:
            return self.max_queue[0] 

    def test(self):
        array = [2,3,4,2,6,2,5,1]
        window_size = 3
        print(array, self.max_in_sliding(array, window_size))
        for item in array:
            self.push_back(item)
        for i in range(len(array)):
            print(self.pop_front(), self.max())


s = Solution()
s.test()
