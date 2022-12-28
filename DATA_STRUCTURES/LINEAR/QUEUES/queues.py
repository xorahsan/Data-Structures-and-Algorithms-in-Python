"""
====================== Queues =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: a list contains all items pushed in Queue
    
Methods:
push(): insert into top of stack
pop(): remove and return top element of stack
print(): print the stack
isEmpty(): return True if Stack is empty else return False
top(): return top element of stack
"""

class Queue:
    def __init__(self):
        self.data = []

    def enQueue(self, item):
        self.data.append(item)

    def deQueue(self):
        return self.data.pop(0)
    
    def front(self):
        return self.data[0]

    def isEmpty(self):
        return self.data == []

    def print(self):
        print(*self.data)

def main():
    q1 = Queue()
    q1.enQueue(5)
    q1.print()
    q1.enQueue(4)
    q1.print()
    q1.enQueue(3)
    q1.print()
    q1.enQueue(2)
    q1.print()
    q1.enQueue(1)
    q1.print()
    q1.deQueue()
    q1.print()
    q1.deQueue()
    q1.print()
    q1.deQueue()
    q1.print()
    q1.deQueue()
    q1.print()


if __name__ == "__main__":
    main()