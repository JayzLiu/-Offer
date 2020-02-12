class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def reverse_linked_list(self, head_node):
        if not head_node or not head_node.next:
            return head_node
        pre = head_node
        cur = head_node.next
        nex = None
        pre.next = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

    def reverse_by_recurence(self, head_node):
        if not head_node or not head_node.next:
            return head_node
        else:
            new_head = self.reverse_by_recurence(head_node.next)
            head_node.next.next = head_node
            head_node.next = None
            return new_head

    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        org_node = None
        new_node = None
        for item in reversed(array):
            new_node = Node(item)
            new_node.next = org_node
            org_node = new_node
        head_node = new_node
        print("original order:")
        while new_node:
            print(new_node.value)
            new_node = new_node.next
        # head_node = self.reverse_linked_list(head_node)
        head_node = self.reverse_by_recurence(head_node)
        print("reversed order:")
        while head_node:
            print(head_node.value)
            head_node = head_node.next

s = Solution()
s.test()
