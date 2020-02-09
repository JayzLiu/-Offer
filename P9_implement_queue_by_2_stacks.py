class Solution(object):
    class Queue(object):
        def __init__(self):
            self.stack1 = []
            self.stack2 = []
        def appendTail(self, item):
            self.stack1.append(item)
        def deleteHead(self):
            if self.stack2:
                return self.stack2.pop()
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
    def test(self):
        array1 = [1,2,3,4,5,6]
        array2 = [11,22,33]
        q = self.Queue()
        print("Appending in the first time")
        for item in array1:
            q.appendTail(item)
        print("Deletion in the first time")
        for i in range(3):
            print(q.deleteHead())
        print("Appending in the second time")
        for item in array2:
            q.appendTail(item)
        print("Deletion in the second time")
        for i in range(6):
            print(q.deleteHead())


s = Solution()
s.test()