from util import binary_tree

class Solution(object):
    def __init__(self):
        self.first_node = None
    
    def convert(self, root):
        # inorder: right mid left
        def convert_BST(root):
            if root is None:
                return None
            convert_BST(root.right)
            if self.first_node:
                self.first_node.left = root
                root.right = self.first_node
                self.first_node = root
            else:
                self.first_node = root
            convert_BST(root.left)
            return self.first_node
        self.first_node = None
        convert_BST(root)
        return self.first_node
    
    def test(self):
        t_pre = [4,2,1,3,6,5,7]
        t_in = [1,2,3,4,5,6,7]
        t = binary_tree.build_binary_tree(t_pre, t_in)
        l = self.convert(t)
        print()


s = Solution()
s.test()
