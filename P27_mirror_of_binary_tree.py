from util import binary_tree

class Solution(object):
    def mirror_of_tree(self, tree_node):
        if not tree_node:
            return tree_node
        temp = tree_node.left
        tree_node.left = self.mirror_of_tree(tree_node.right)
        tree_node.right = self.mirror_of_tree(temp)
        return tree_node
    
    def test(self):
        t_pre = [1,2,5,6,3]
        t_in = [5,2,6,1,3]
        t = binary_tree.build_binary_tree(t_pre, t_in)
        t = self.mirror_of_tree(t)
        print("preorder after mirrorize")
        binary_tree.print_preorder_array(t)
        print("inorder after mirrorize")
        binary_tree.print_inorder_array(t)


s = Solution()
s.test()