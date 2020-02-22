from util.binary_tree import *

class Solution(object):
    def get_lowest_ancestor(self, tree, node1, node2):
        if not (tree and node1 and node2):
            return None
        path1, path2 = [], [] 
        res1 = self.get_path(tree, node1, path1)
        res2 = self.get_path(tree, node2, path2)
        if not (res1 and res2):
            return None
        min_len = min(len(path1), len(path2))
        i = 0
        while i < min_len and path1[i] == path2[i]:
            i += 1
        return path1[i - 1]

    def get_path(self, root, node, path):
        if root == None:
            return False
        if root == node:
            path.append(node)
            return True
        path.append(root)
        left = self.get_path(root.left, node, path)
        if left:
            return True
        else:
            right = self.get_path(root.right, node, path)
            if right:
                return True
            else:
                path.pop()
                return False

    def test(self):
        preorder = [1,2,4,8,9,5,10,11,3,6,7]
        inorder = [8,4,9,2,10,5,11,1,6,3,7]
        t = build_binary_tree(preorder, inorder)
        node1 = get_node(t, 4)
        node2 = get_node(t, 10)
        ancestor = self.get_lowest_ancestor(t, node1, node2)
        print(node1.value, node2.value, ancestor.value)

    
s = Solution()
s.test()
