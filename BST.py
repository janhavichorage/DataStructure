
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

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


# Count total nodes
def count_nodes(temp):
    if temp is None:
        return 0
    else:
        return 1 + count_nodes(temp.left) + count_nodes(temp.right)


# Count leaf nodes
def count_leaf(temp):
    if temp is None:
        return 0
    elif temp.left is None and temp.right is None:
        return 1
    else:
        return count_leaf(temp.left) + count_leaf(temp.right)


# Count non-leaf nodes
def count_nonleaf(temp):
    if temp is None:
        return 0
    elif temp.left is None and temp.right is None:
        return 0
    else:
        return 1 + count_nonleaf(temp.left) + count_nonleaf(temp.right)

def find_minmax(self,rt):
    temp=rt
    while temp.temp.left:
        temp=temp.left
    print("\nmin value:",temp.data)
    temp=rt
    while temp.right:
        temp=temp.right
    print("\nMax value:",temp.data)
btree = BST()

btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))
btree.find_minmax()

print("Total Nodes:", count_nodes(btree.root))
print("Leaf Nodes:", count_leaf(btree.root))
print("Non-Leaf Nodes:", count_nonleaf(btree.root))
