from util import binary_tree


class Solution(object):
    def is_substructure(self, tree1, tree2):
        if not tree1 or not tree2:
            return False
        res = False
        if tree1.value == tree2.value:
            res = self.compare(tree1, tree2)
        if res:
            return True
        else:
            if self.is_substructure(tree1.left, tree2):
                return True
            elif self.is_substructure(tree1.right, tree2):
                return True
            else:
                return False
    
    def compare(self, sub_tree1, sub_tree2):
        if not sub_tree2:
            return True
        elif not sub_tree1:
            return False
        if sub_tree1.value == sub_tree2.value:
            return self.compare(sub_tree1.left, sub_tree2.left) and self.compare(sub_tree1.right, sub_tree2.right)
        else:
            return False
    
    def test(self):
        t1_pre = [1,2,4,5,3,6,7]
        t1_in = [4,2,5,1,6,3,7]
        t2_pre = [3, 6, 7]
        t2_in = [6, 3, 7]
        t1= binary_tree.build_binary_tree(t1_pre, t1_in)
        t2= binary_tree.build_binary_tree(t2_pre, t2_in)
        print(self.is_substructure(t1, t2))


s = Solution()
s.test()

    