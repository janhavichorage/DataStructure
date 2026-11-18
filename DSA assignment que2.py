
# Linear Queue Implementation

class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue
    def enqueue(self, element):
        self.queue.append(element)

    # 2. Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            element = self.queue.pop(0)
            print("Deleted element:", element)

    # 3. Display
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue)

    # 4. Reverse Queue using Stack
    def reverse(self):
        stack = []

        while len(self.queue) > 0:
            stack.append(self.queue.pop(0))

        while len(stack) > 0:
            self.queue.append(stack.pop())

    # 5. Merge Two Queues
    def merge(self, q2):
        new_queue = Queue()

        for i in self.queue:
            new_queue.enqueue(i)

        for i in q2.queue:
            new_queue.enqueue(i)

        return new_queue

    # 6. Check Identical Queues
    def identical(self, q2):
        if self.queue == q2.queue:
            print("Both queues are identical")
        else:
            print("Both queues are not identical")


# Creating Queue Objects
q1 = Queue()
q2 = Queue()

# Enqueue Elements
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print("First Queue:")
q1.display()

# Dequeue
q1.dequeue()

print("\nQueue After Dequeue:")
q1.display()

# Second Queue
q2.enqueue(50)
q2.enqueue(60)

# Reverse Queue
q1.reverse()

print("\nReversed Queue:")
q1.display()

# Merge Queues
q3 = q1.merge(q2)

print("\nMerged Queue:")
q3.display()

# Check Identical
print("\nIdentical Queue Checking:")
q1.identical(q2)
