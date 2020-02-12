from util import binary_tree

class Solution(object):

    def is_symetrical_by_recurence(self, tree_node):
        return self.is_symetrical_core(tree_node, tree_node)
        
    def is_symetrical_core(self, node1, node2):
        if not node1 and not node2:
            return True        
        elif not node1 or not node2:
            return False
        elif node1.value != node2.value:
            return False
        else:
            return self.is_symetrical_core(node1.left, node2.right) and \
              self.is_symetrical_core(node1.right, node2.left)

    def test(self):
        pass

