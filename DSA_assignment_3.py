class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    # 1. Add Patient (Enqueue)
    def enqueue(self, new_node):

        if self.front == None:
            self.front = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        print("Patient added successfully")

    # 2. Display Next Patient
    def display_next(self):

        if self.front == None:
            print("Queue is empty")
        else:
            print("Next Patient:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):

        if self.front:
            temp = self.front

            print("Patient treated:")
            print("ID:", temp.pid)
            print("Name:", temp.name)

            self.front = self.front.next
        else:
            print("Queue is empty")

    # 4. Display All Patients
    def display_all(self):

        temp = self.front

        if temp == None:
            print("No waiting patients")
            return

        print("Patients in Priority Order:")

        while temp:
            print("ID:", temp.pid,
                  "Name:", temp.name,
                  "Priority:", temp.priority)

            temp = temp.next


# Create Priority Queue
pq = PriorityQueue()

while True:

    print("\n--- HOSPITAL EMERGENCY MANAGEMENT ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        pr = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if pr >= 1 and pr <= 3:
            pq.enqueue(Node(pid, name, pr))
        else:
            print("Invalid Priority")

    elif ch == 2:
        pq.display_next()

    elif ch == 3:
        pq.dequeue()

    elif ch == 4:
        pq.display_all()

    elif ch == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")