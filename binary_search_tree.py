class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insert(root, node):
    if root is None:
        root = node
    else:
        if node.val >= root.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def show(node):
    if node:
        show(node.left)
        print node.val
        show(node.right)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))
show(r)