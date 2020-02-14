from util import linked_list

class Solution(object):
    def copy(self, head):
        # Timt: O(n)
        # Space: O(n)
        if not head:
            return None
        cur_org = head
        map = {}
        pre_copy = linked_list.Node(cur_org.value)
        copy_head = pre_copy
        map[cur_org] = pre_copy
        cur_org = cur_org.next
        while cur_org:
            cur_copy = linked_list.Node(cur_org.value)
            pre_copy.next = cur_copy
            map[cur_org] = cur_copy
            pre_copy = cur_copy
            cur_org = cur_org.next
        cur_org = head
        while cur_org:
            if cur_org.sibling:
                map[cur_org].sibling = map[cur_org.sibling]
            cur_org = cur_org.next
        return copy_head

    def copy_v2(self, head):
        # Time: O(n)
        # Space: O(1)
        if not head:
            return None
        self.copy_nodes(head)
        self.connect_sibling(head)
        return self.split_out_lists(head)

    def copy_nodes(self, head):
        cur_org = head
        while cur_org:
            cur_copy = linked_list.Node(cur_org.value)
            cur_copy.next = cur_org.next
            cur_org.next = cur_copy
            cur_org = cur_org.next.next

    def connect_sibling(self, head):
        cur_org = head
        while cur_org:
            if cur_org.sibling:
                cur_org.next.sibling = cur_org.sibling.next
            cur_org = cur_org.next.next

    def split_out_lists(self, head):
        copy_head = head.next
        pre_org = head
        cur_org = head.next.next
        pre_copy = copy_head
        while cur_org:
            pre_copy.next = cur_org.next
            pre_org.next = cur_org
            pre_copy = pre_copy.next
            pre_org = cur_org
            cur_org = cur_org.next.next
        return copy_head

    def test(self):
        array = [0,1,2,3,4,5]
        nodes = []
        org_list = linked_list.init_list(array, nodes)
        nodes[1].sibling = nodes[3]
        nodes[4].sibling = nodes[5]
        copy_list1 = self.copy(org_list)
        copy_list2 = self.copy_v2(org_list)
        print()


s = Solution()
s.test()
