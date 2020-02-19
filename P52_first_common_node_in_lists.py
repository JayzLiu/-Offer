from util.linked_list import init_list

class Solution(object):
    def get_common_node(self, list1, list2):
        def length(list):
            count = 0
            while list:
                list = list.next
                count += 1
            return count
        if not list1 or not list2:
            return None
        len1 = length(list1)
        len2 = length(list2)
        if len1 < len2:
            short, long = list1, list2
            diff = len2 - len1
        else:
            short, long = list2, list1
            diff = len1 - len2
        for i in range(diff):
            long = long.next
        while short and long and short != long:
            short = short.next
            long = long.next
        return short

    def test(self):
        array1 = [1,3,5,7]
        array2 = [2,4,6,8,9,10]
        nodes1 = []
        nodes2 = []
        l1 = init_list(array1, nodes1)
        l2 = init_list(array2, nodes2)
        nodes1[-1].next = nodes2[-2]
        cnode = self.get_common_node(l1, l2)
        print(cnode.value)
        

s = Solution()
s.test()
    