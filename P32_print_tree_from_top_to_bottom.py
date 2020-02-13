from util import binary_tree
class Solution(object):
    def print_tree(self, tree):
        arr_to_print = []
        if not tree:
            print(arr_to_print)
            return
        queue = [tree]
        while queue:
            cur_node = queue.pop(0)
            arr_to_print.append(cur_node.value)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print(arr_to_print)

    def print_tree_in_lines(self, tree):
        if not tree:
            return
        queue = [tree]
        left_in_cur_level = 1
        node_in_next_level = 0
        while queue:
            cur_node = queue.pop(0)
            print(str(cur_node.value) + ' ' , end='')
            if cur_node.left:
                queue.append(cur_node.left)
                node_in_next_level += 1
            if cur_node.right:
                queue.append(cur_node.right)
                node_in_next_level += 1
            left_in_cur_level -= 1
            if left_in_cur_level == 0:
                print()
                left_in_cur_level = node_in_next_level
                node_in_next_level = 0

    def print_tree_in_zigzag(self, tree):
        if not tree:
            return
        stacks = [[], []]
        cur = 0
        nex = 1 - cur
        stacks[cur].append(tree)
        while stacks[cur] or stacks[nex]:
            cur_node = stacks[cur].pop()
            print(str(cur_node.value) + ' ', end='')
            if cur == 0:
                if cur_node.left:
                    stacks[nex].append(cur_node.left)
                if cur_node.right:
                    stacks[nex].append(cur_node.right)
            else:
                if cur_node.right:
                    stacks[nex].append(cur_node.right)
                if cur_node.left:
                    stacks[nex].append(cur_node.left)
            if len(stacks[cur]) == 0:
                print()
                cur = nex
                nex = 1 - cur


    def test(self):
        t_pre = [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15]
        t_in = [8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]
        t = binary_tree.build_binary_tree(t_pre, t_in)
        self.print_tree(t)
        self.print_tree_in_lines(t)
        self.print_tree_in_zigzag(t)


s = Solution()
s.test()