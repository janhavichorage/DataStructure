
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Append node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at specific position
    def insert_at(self, pos, data):
        if pos < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node value:", slow.data)
        else:
            print("List is empty")

    # 5. Delete node by value
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
        else:
            print("Value not found")

    # 6. Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # 7. Sum of consecutive pairs
    def sum_consecutive_pairs(self):
        temp = self.head

        while temp and temp.next:
            print(
                f"Sum({temp.data}, {temp.next.data}) = "
                f"{temp.data + temp.next.data}"
            )
            temp = temp.next

    # 8. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 9. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # 10. Delete middle node
    def delete_middle(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

    # 11. Delete alternate nodes
    def delete_alternate(self):
        temp = self.head

        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next

    # 12. Concatenate two linked lists
    def concatenate(self, ll2):
        if self.head is None:
            self.head = ll2.head
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = ll2.head


# Main Program

# First linked list
ll1 = LinkedList()
ll1.append(10)
ll1.append(20)
ll1.append(30)
ll1.append(40)
ll1.append(50)

print("First Linked List:")
ll1.traverse()

# Second linked list
ll2 = LinkedList()
ll2.append(60)
ll2.append(70)
ll2.append(80)

print("\nSecond Linked List:")
ll2.traverse()

# Concatenate two linked lists
ll1.concatenate(ll2)

print("\nAfter concatenation:")
ll1.traverse()
