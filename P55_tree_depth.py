from util.binary_tree import build_binary_tree

class Solution(object):
    def depth_of_tree(self, tree):
        def depth(node):
            if node == None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            return 1 + max(left, right)
        if not tree:
            return None
        return depth(tree)

    def is_balance(self, tree):
        # preorder
        def depth(node):
            if node == None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            return 1 + max(left, right)
        if tree == None:
            return True
        left = depth(tree.left)
        right = depth(tree.right)
        diff = left - right
        if diff < -1 or 1 < diff:
            return False
        return self.is_balance(tree.left) and self.is_balance(tree.right)

    def is_balance_postorder(self, tree):
        def is_balance_core(node):
            if not node:
                return 0
            left = is_balance_core(node.left)
            right = is_balance_core(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)
        if not tree:
            return False
        elif is_balance_core(tree):
            return True
        else:
            return False

    def test(self):
        preorder = [1,2,4,5,7,3,6]
        inorder = [4,2,7,5,1,3,6]
        t = build_binary_tree(preorder, inorder)
        print(self.depth_of_tree(t))
        print(self.is_balance(t))
        preorder = [1,2,3]
        inorder = [1,2,3]
        t = build_binary_tree(preorder, inorder)
        print(self.is_balance(t))


s = Solution()
s.test()