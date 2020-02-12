class Solution(object):
    class BinaryTreeNode(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None  # Initialing for Problem 8

    def print_preorder_array(self, node):
        if node != None:
            print(node.value)
            self.print_preorder_array(node.left)
            self.print_preorder_array(node.right)
        else:
            return

    def print_inorder_array(self, node):
        if node != None:
            self.print_inorder_array(node.left)
            print(node.value)
            self.print_inorder_array(node.right)
        else:
            return

    def print_postorder_array(self, node):
        if node != None:
            self.print_postorder_array(node.left)
            self.print_postorder_array(node.right)
            print(node.value)
        else:
            return

    def test(self):
        preorder_array = [1, 2, 4, 7, 3, 5, 6, 8]
        inorder_array = [4, 7, 2, 1, 5, 3, 8, 6]
        tree_root = self.rebuild_binary_tree(preorder_array, inorder_array)
        print("preorder after rebuliding:")
        self.print_preorder_array(tree_root)
        print("inorder after rebuliding:")
        self.print_inorder_array(tree_root)
        print("postorder after rebuliding:")
        self.print_postorder_array(tree_root)

    def rebuild_binary_tree(self, preorder_array, inorder_array):
        tree_root = self.construct_core(preorder_array, inorder_array)
        return tree_root

    def construct_core(self, preorder, inorder):
        assert len(preorder) == len(inorder)
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            root = self.BinaryTreeNode(preorder[0])
            return root
        else:
            split_index = inorder.index(preorder[0])
            root = self.BinaryTreeNode(preorder[0])
            root.left = self.construct_core(preorder[1:split_index+1], inorder[:split_index])
            root.right = self.construct_core(preorder[split_index+1:], inorder[split_index+1:])
            return root

if __name__ == "__main__":
    s = Solution()
    s.test()