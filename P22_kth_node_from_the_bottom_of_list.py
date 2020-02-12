class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def get_the_k_node_from_bottom(self, head_node, k):
        if not head_node or not k:
            return None
        i = 1
        ahead_node = head_node
        while i <= k and ahead_node.next:
            ahead_node = ahead_node.next
            i += 1
        if i < k:
            return None
        behind_node = head_node
        while ahead_node:
            ahead_node = ahead_node.next
            behind_node = behind_node.next
        return behind_node

    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        # array = []
        org_node = None
        new_node = None
        for item in reversed(array):
            new_node = Node(item)
            new_node.next = org_node
            org_node = new_node
        list_node = new_node
        k_node = self.get_the_k_node_from_bottom(list_node, 1)
        if k_node: print(k_node.value)


s = Solution()
s.test()
