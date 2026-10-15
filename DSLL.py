
class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        temp = self.head

        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def print(self):
        temp = self.head
        print("List elements:")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def print_reverse(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        print("Reverse list elements:")

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


list1 = Linkedlist()

list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.append(Node(16))

list1.insert(Node(99), 3)

list1.print()
list1.print_reverse()
