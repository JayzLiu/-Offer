from util import binary_tree

class Solution(object):
    def __init__(self):
        self.stream = []
        self.index = 0

    def serialize(self, root):
        def serialize_core(node):
            if node == None:
                self.stream.append('$')
            else:
                self.stream.append(str(node.value))
                serialize_core(node.left)
                serialize_core(node.right)
            return
        self.stream = []
        serialize_core(root)
        return self.stream

    def deserialize(self, stream):
        def deserialize_core(stream):
            if self.index >= len(stream):
                return
            if stream[self.index] != '$':
                cur_node = binary_tree.BinaryTreeNode(int(stream[self.index]))
                self.index += 1
                cur_node.left = deserialize_core(stream)
                cur_node.right = deserialize_core(stream)
                return cur_node
            else:
                self.index += 1
                return None
        self.index = 0
        return deserialize_core(stream)

    def test(self):
        preorder = [1,2,4,3,5,6]
        inorder = [4,2,1,5,3,6]
        t = binary_tree.build_binary_tree(preorder, inorder)
        stream = self.serialize(t)
        print(stream)
        ut = self.deserialize(stream)
        print("preorder after deserializing")
        binary_tree.print_preorder_array(ut)
        print("inorder after deserializing")
        binary_tree.print_inorder_array(ut)


s = Solution()
s.test()
