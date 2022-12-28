
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
    