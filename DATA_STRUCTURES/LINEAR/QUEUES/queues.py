"""
====================== Queues =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: a list contains all items pushed in Queue
    
Methods:
enQueue(): insert into queue
deQueue(): remove and return front of queue
print(): print the queue
isEmpty(): return True if Queue is empty else return False
front(): return front element of queue
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