class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        value_to_delete = 3
        node_to_delete = None
        specified_node = [value_to_delete, node_to_delete]
        head_node = self.init_linked_list(array, specified_node)
        node_to_delete = specified_node[1]
        self.print_linked_list(self.delete_node_in_linked_list(head_node, node_to_delete))
        print("Delete duplicated node in linked list")
        array = [0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7]
        head_node = self.init_linked_list(array)
        self.print_linked_list(self.delete_duplicated_node_in_linked_list(head_node))

    def init_linked_list(self, array, specified_node=[None, None]):
        value_to_delete = specified_node[0] # first item for input, second item for output
        org_node = None
        new_node = None
        for item in reversed(array):
            new_node = Node(item)
            if item == value_to_delete:
                specified_node[1] = new_node
            new_node.next = org_node
            org_node = new_node
        head_node = new_node
        return head_node

    def print_linked_list(self, head_node):
        cur_node = head_node
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def delete_node_in_linked_list(self, head_node, node_to_delete):
        if not (head_node and node_to_delete):
            return None
        if head_node == node_to_delete:
            head_node = None
        elif node_to_delete.next != None:
            # Not the last node
            node_to_delete.value = node_to_delete.next.value
            node_to_delete.next = node_to_delete.next.next
        else:
            pre_node = head_node
            while pre_node.next != node_to_delete:
                pre_node = pre_node.next
            pre_node.next = None
        return head_node

    def delete_duplicated_node_in_linked_list(self, head_node):
        if head_node == None or head_node.next == None:
            return False
        new_head = Node(-1)
        new_head.next = head_node
        pre_node = new_head
        cur_node = new_head.next
        while cur_node:
            if cur_node.next and cur_node.value == cur_node.next.value:
                while cur_node.next and cur_node.value == cur_node.next.value:
                    cur_node = cur_node.next
                pre_node.next = cur_node.next
                cur_node = pre_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return new_head.next


s = Solution()
s.test()
