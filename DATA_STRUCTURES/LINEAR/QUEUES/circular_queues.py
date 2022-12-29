"""
====================== Circular Queues =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: a list contains all items pushed in Queue
    length: length of queue
    size: count of enqueued items
    head: head index of queue
    tail: tail index of queue

Methods:
enQueue(): insert into queue
deQueue(): remove and return front of queue
print(): print the queue
isEmpty(): return True if Queue is empty else return False
isFull(): return True if Queue is full as per its length else return False
front(): return front element of queue
rear(): return back element of queue

"""

class CircularQueue:

    def __init__(self, n):
        self.data = [None for i in range(n)]
        self.length = n
        self.size = 0
        self.head = 0
        self.tail = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.length

    def enQueue(self, item):
        if self.isFull():
            return print("QUEUE is full")
        self.data[self.tail] = item
        self.tail = (self.tail+1)%self.length
        self.size +=1
        

    def deQueue(self):
        if self.isEmpty():
            return print("QUEUE is empty")
        temp = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head+1) % self.length
        self.size -=1
        return temp

    def front(self):
        return self.data[self.head]

    def rear(self):
        return self.data[self.tail]

    def print(self):
        print(*self.data)
        print("Head Index => ", self.head)
        print("Tail Index => ", self.tail)

def main():

    cq = CircularQueue(5)
    cq.enQueue(1)
    cq.enQueue(2)
    cq.enQueue(3)
    cq.print()
    cq.deQueue()
    cq.print()
    cq.enQueue(4)
    cq.enQueue(5)
    cq.print()
    cq.enQueue(1)
    cq.print()
    cq.deQueue()
    cq.print()
    cq.deQueue()
    cq.print()

if __name__ == "__main__":
    main()
    