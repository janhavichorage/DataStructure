
# Binary Search Tree

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right


# Inorder Traversal (Left Root Right)
def inorder(temp):
    if temp is None:
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


# Preorder Traversal (Root Left Right)
def preorder(temp):
    if temp is None:
        return

    print(temp.data, end=" ")
    preorder(temp.left)
    preorder(temp.right)


# Postorder Traversal (Left Right Root)
def postorder(temp):
    if temp is None:
        return

    postorder(temp.left)
    postorder(temp.right)
    print(temp.data, end=" ")


# Count Total Nodes
def count_nodes(temp):
    if temp is None:
        return 0

    return 1 + count_nodes(temp.left) + count_nodes(temp.right)


# Count Leaf Nodes
def count_leaf(temp):
    if temp is None:
        return 0

    if temp.left is None and temp.right is None:
        return 1

    return count_leaf(temp.left) + count_leaf(temp.right)


# Count Non-Leaf Nodes
def count_nonleaf(temp):
    if temp is None:
        return 0

    if temp.left is None and temp.right is None:
        return 0

    return 1 + count_nonleaf(temp.left) + count_nonleaf(temp.right)


# Main Program
btree = BST()

btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))

print("Inorder Traversal:")
inorder(btree.root)

print("\nPreorder Traversal:")
preorder(btree.root)

print("\nPostorder Traversal:")
postorder(btree.root)

print("\n\nTotal Nodes:", count_nodes(btree.root))
print("Leaf Nodes:", count_leaf(btree.root))
print("Non-Leaf Nodes:", count_nonleaf(btree.root))
