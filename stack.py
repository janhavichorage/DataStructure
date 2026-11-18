
# Stack Implementation using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # 1. Push Operation
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # 2. Pop Operation
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next
            temp = None

    # 3. Display Operation
    def print(self):
        if self.isempty():
            print("Stack is empty...")
        else:
            print("Stack contains")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    # 4. Reverse String using Stack
    def reverse_string(self, string):
        s = stack()

        for ch in string:
            s.push(Node(ch))

        result = ""

        while not s.isempty():
            result = result + s.top.data
            s.top = s.top.next

        print("Reversed string:", result)

    # 5. Reverse Stack using Another Stack
    def reverse(self, st1):
        temp = self.top

        while temp:
            st1.push(Node(temp.data))
            temp = temp.next


# Creating Stack Objects
st = stack()
st1 = stack()

# Push Elements
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

# Display Stack
st.print()

# Pop Operation
st.pop()

# Display After Pop
st.print()

# Reverse String
st.reverse_string("PYTHON")

# Reverse Stack using Another Stack
st.reverse(st1)

# Display Reversed Stack
print("Reversed Stack:")
st1.print()
