class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def get_the_entry_node(self, head_node):
        if not head_node or not head_node.next:
            return None
        ahead_node = head_node.next.next
        behind_node = head_node
        while ahead_node and ahead_node.next and ahead_node != behind_node:
            ahead_node = ahead_node.next.next
            behind_node = behind_node.next
        if ahead_node != behind_node:
            # No Circle
            return None
        else:
            met_node = ahead_node
            cur_node = met_node.next
            ahead_node = head_node.next
            while met_node != cur_node:
                cur_node = cur_node.next
                ahead_node = ahead_node.next
            behind_node = head_node
            while ahead_node != behind_node:
                ahead_node = ahead_node.next
                behind_node = behind_node.next
            return ahead_node

    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        org_node = None
        new_node = None
        array.reverse()
        for i in range(len(array)):
            new_node = Node(array[i])
            if i == 0:
                tail_node = new_node
            if i == len(array) // 2:
                entry_node = new_node
            new_node.next = org_node
            org_node = new_node
        print("entry_node: " + str(entry_node.value))
        tail_node.next = entry_node
        list_node = new_node
        res = self.get_the_entry_node(list_node)
        # res = self.get_the_entry_node(Node(1))
        if res:
            print(res.value)


s = Solution()
s.test()
