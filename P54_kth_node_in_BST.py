from util.binary_tree import build_binary_tree

class Solution(object):
    def __init__(self):
        self.count = 0

    def get_the_k_node(self, tree, k):
        def inorder_traverse(node, k):
            target = None
            if node.left:
                target = inorder_traverse(node.left, k)
            if not target:
                if self.count == k - 1:
                    return node
                else:
                    self.count += 1
            if not target and node.right:
                target = inorder_traverse(node.right, k)
            return target
        self.count = 0
        if not tree or not k:
            return None
        return inorder_traverse(tree, k)

    def test(self):
        preorder = [4,2,1,3,6,5,7]
        inorder = [1,2,3,4,5,6,7]
        t = build_binary_tree(preorder, inorder)
        k = 3
        print(k, self.get_the_k_node(t, k).value)


s = Solution()
s.test()