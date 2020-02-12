class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):

    def print_node_by_stack(self, node):
        stack = []
        cur_node = node
        while cur_node != None:
            stack.append(cur_node.value)
            cur_node = cur_node.next
        while stack:
            print(stack.pop())

    def print_node_by_recurrence(self, node):
        if node.next:
            self.print_node_by_recurrence(node.next)
            print(node.value)
        else:
            print(node.value)

    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        org_node = None
        new_node = None
        for item in reversed(array):
            new_node = ListNode(item)
            new_node.next = org_node
            org_node = new_node
        list_node = new_node
        print("original order:")
        while new_node:
            print(new_node.value)
            new_node = new_node.next
        print("reversed order by stack")
        self.print_node_by_stack(list_node)
        print("reversed order by recurrence")
        self.print_node_by_recurrence(list_node)


s = Solution()
s.test()