import P7_rebuild_binary_tree


class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class Solution(object):

    def build_link_from_child(self, node):
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node

    def traverse_to_build_link(self, root):
        if root:
            self.traverse_to_build_link(root.left)
            self.traverse_to_build_link(root.right)
            self.build_link_from_child(root)

    def find_node(self, root, value, node):
        # node is a list
        if root:
            if value == root.value:
                node[0] = root
                return True
            if self.find_node(root.left, value, node):
                return True
            if self.find_node(root.right, value, node):
                return True
        else:
            return False

    def find_next_node(self, node):
        if node == None:
            return None
        if node.right:
            potential_successor = node.right
            while potential_successor.left:
                potential_successor = potential_successor.left
            return potential_successor
        else:
            potential_successor = node
            while potential_successor.parent and potential_successor != potential_successor.parent.left:
                potential_successor = potential_successor.parent
            return potential_successor.parent

    def test(self):
        p7_s = P7_rebuild_binary_tree.Solution()
        preorder_array = [1, 2, 4, 7, 3, 5, 6, 8]
        inorder_array = [4, 7, 2, 1, 5, 3, 8, 6]
        tree_root = p7_s.rebuild_binary_tree(preorder_array, inorder_array)
        self.traverse_to_build_link(tree_root)
        target = [None]
        self.find_node(tree_root, 6, target)
        target_node = target[0]
        assert target_node != None
        print(target_node.value)
        successor = self.find_next_node(target_node)
        if successor:
            print(successor.value)


s = Solution()
s.test()