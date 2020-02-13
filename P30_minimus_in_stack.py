class Solution(object):
    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def min(self):
        if self.aux_stack:
            return self.aux_stack[-1]
        else:
            return None
    
    def push(self, value):
        self.stack.append(value)
        if len(self.aux_stack) == 0 or self.aux_stack[-1] > value:
            self.aux_stack.append(value)
        else:
            self.aux_stack.append(self.aux_stack[-1])

    def pop(self):
        assert len(self.stack) == len(self.aux_stack)
        if self.stack:
            self.aux_stack.pop()
            return self.stack.pop()
        else:
            return None

    def test(self):
        self.push(3)
        print(self.stack, self.aux_stack)
        self.push(2)
        print(self.stack, self.aux_stack)
        self.push(3)
        print(self.stack, self.aux_stack)
        self.push(1)
        print(self.stack, self.aux_stack)
        print(self.pop())
        print(self.stack, self.aux_stack)


s = Solution()
s.test()


