class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def init_list(array):
    org_node = None
    new_node = None
    for item in reversed(array):
        new_node = Node(item)
        new_node.next = org_node
        org_node = new_node
    return new_node

def print_list(head_node):
    while head_node:
        print(head_node.value)
        head_node = head_node.next