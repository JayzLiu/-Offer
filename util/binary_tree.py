class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree(preorder_array, inorder_array):
    def construct_core(preorder, inorder):
        assert len(preorder) == len(inorder)
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            root = BinaryTreeNode(preorder[0])
            return root
        else:
            split_index = inorder.index(preorder[0])
            root = BinaryTreeNode(preorder[0])
            root.left = construct_core(preorder[1:split_index+1], inorder[:split_index])
            root.right = construct_core(preorder[split_index+1:], inorder[split_index+1:])
            return root
    tree_root = construct_core(preorder_array, inorder_array)
    return tree_root

def print_preorder_array(node):
        if node != None:
            print(node.value)
            print_preorder_array(node.left)
            print_preorder_array(node.right)
        else:
            return

def print_inorder_array(node):
    if node != None:
        print_inorder_array(node.left)
        print(node.value)
        print_inorder_array(node.right)
    else:
        return

def print_postorder_array(node):
    if node != None:
        print_postorder_array(node.left)
        print_postorder_array(node.right)
        print(node.value)
    else:
        return



