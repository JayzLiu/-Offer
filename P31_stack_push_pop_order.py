class Solution(object):
    def is_legal_order(self, push_order, pop_order):
        if len(push_order) != len(pop_order):
            return False
        if not push_order or not pop_order:
            return False
        index = 0
        aux_stack = []
        for num in pop_order:
            if aux_stack and aux_stack[-1] == num:
                aux_stack.pop()
            else:
                while index < len(push_order) and push_order[index] != num:
                    aux_stack.append(push_order[index])
                    index += 1
                if index >= len(push_order):
                    return False
                else:
                    index += 1
        if len(aux_stack) == 0:
            return True
        else:
            return False
    
    def test(self):
        push_order = [1,2,3,4,5]
        pop_order = [3,2,1,4,5]
        print(push_order, pop_order, self.is_legal_order(push_order, pop_order))
        pop_order = [3,2,1]
        print(push_order, pop_order, self.is_legal_order(push_order, pop_order))
        pop_order = [4,5,3,2,1]
        print(push_order, pop_order, self.is_legal_order(push_order, pop_order))
                
s = Solution()
s.test()