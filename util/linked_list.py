class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.sibling = None

def init_list(array, nodes_array=None):
    org_node = None
    new_node = None
    for item in reversed(array):
        new_node = Node(item)
        new_node.next = org_node
        if nodes_array != None:
            nodes_array.append(new_node)
        org_node = new_node
    if nodes_array:
        nodes_array.reverse()
    return new_node

def print_list(head_node):
    while head_node:
        print(head_node.value)
        head_node = head_node.next