from util import linked_list

class Solution(object):
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None
        cur_of_l1 = list1
        cur_of_l2 = list2
        merged_list = None
        if cur_of_l1.value <= cur_of_l2.value:
            merged_list = cur_of_l1
            cur_of_l1 = cur_of_l1.next
        else:
            merged_list = cur_of_l2
            cur_of_l2 = cur_of_l2.next
        cur_of_ml = merged_list
        while cur_of_l1 and cur_of_l2:
            if cur_of_l1.value <= cur_of_l2.value:
                cur_of_ml.next = cur_of_l1
                cur_of_l1 = cur_of_l1.next
            else:
                cur_of_ml.next = cur_of_l2
                cur_of_l2 = cur_of_l2.next
            cur_of_ml = cur_of_ml.next
        if cur_of_l1:
            cur_of_ml.next = cur_of_l1
        if cur_of_l2:
            cur_of_ml.next = cur_of_l2
        return merged_list

    def merge_by_recurence(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None
        if list1.value <= list2.value:
            merged_head = list1
            merged_head.next = self.merge_by_recurence(list1.next, list2)
        else:
            merged_head = list2
            merged_head.next = self.merge_by_recurence(list1, list2.next)
        return merged_head

    def test(self):
        array1 = [1,3,5,7]
        array2 = [2,4,6,8]
        # array2 = []
        list1 = linked_list.init_list(array1)
        list2 = linked_list.init_list(array2)
        merged_list = self.merge_by_recurence(list1, list2)
        linked_list.print_list(merged_list)


s = Solution()
s.test()