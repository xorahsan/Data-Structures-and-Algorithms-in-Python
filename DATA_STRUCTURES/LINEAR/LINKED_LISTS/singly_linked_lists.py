class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, item):
        self.head = Node(item, self.head)

    def insertAtEnd(self, item):
        if not self.head:  return self.insertAtBegin(item)
        i = self.head
        while i.next: i = i.next
        i.next = Node(item)
        
    def length(self):
        i, j = 0,self.head
        while j: i,j = i+1,j.next
        return i

    def removeAt(self, ind):
        if ind < 0 or ind >= self.length(): return print("INVALID Index")
        if ind == 0:
            self.head = self.head.next
            return
        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = None if i == self.length()-2 else j.next.next

    def insertAt(self, ind, item):
        if ind < 0 or ind > self.length(): return print("INVALID Index")
        if ind == self.length(): return self.insertAtEnd(item)
        if ind == 0: return self.insertAtBegin(item)

        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = Node(item) if not j.next else Node(item,j.next)

    def print(self):
        if not self.head: return print("Linked List is empty")
        i = self.head
        while i:
            print(i.data, end=" => ")
            i = i.next
        print()
        
def main():
    sll = SinglyLinkedList()
    sll.insertAtEnd(6)
    sll.print()
    print(sll.length())
    sll.insertAtBegin(6)
    sll.print()
    sll.removeAt(0)
    sll.print()
    sll.insertAtEnd(5)
    print(sll.length())
    sll.insertAtBegin(4)
    sll.print()
    print(sll.length())
    sll.insertAtBegin(3)
    sll.print()
    print(sll.length())
    sll.insertAtEnd(7)
    sll.print()
    print(sll.length())
    sll.insertAtEnd(8)
    sll.print()
    print(sll.length())
    sll.insertAtEnd(9)  
    sll.print()
    print(sll.length())
    sll.removeAt(0)
    sll.print()
    sll.insertAt(6, 0)
    sll.print()

if __name__ == "__main__":
    main()

