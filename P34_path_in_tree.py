from util import binary_tree
class Solution(object):
    def __init__(self):
        self.all_paths = []
        self.cur_path = []
    def find_path_equal_sum(self, node, sum):
        def find_path(node, sum):
            if not node:
                return
            sum -= node.value
            is_leaf = not node.left and not node.right
            if is_leaf and sum == 0:
                self.cur_path.append(node.value)
                self.all_paths.append(self.cur_path[:])  # slicing for shallow copy
                self.cur_path.pop()
                return
            if not is_leaf and sum > 0:
                self.cur_path.append(node.value)
                if node.left:
                    find_path(node.left, sum)
                if node.right:
                    find_path(node.right, sum)
                return
            else:
                return
        self.all_paths = []
        self.cur_path = []
        find_path(node, sum)
        return self.all_paths

    def test(self):
        preorder = [10, 5, 4, 7, 12]
        inorder = [4, 5, 7, 10, 12]
        t = binary_tree.build_binary_tree(preorder, inorder)
        print(self.find_path_equal_sum(t, 22))
        print(self.find_path_equal_sum(t, 10))


s = Solution()
s.test()
