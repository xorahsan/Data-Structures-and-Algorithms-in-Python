
"""
======================= Circular Singly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Node class Variables:
    value: value of current node
    next: whole next Node

Circular Singly List class variables:
    head: the whole node of current circular singly linked list head


Circular Singly Linked List Methods:

insertAtBegin(data) # insert Node at start

printAll() # print every element of current linked list

print(reverse=True) #print doubly linked list in reverse order

length() # return length of current Linked List

insertAtEnd(data) # insert Node at end

insertAt(index, data) # insert Node at the given index

removeAt(index) #remove Node by Index

find(data) #return index of first occurence of given value

"""

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, item):
        if not self.head:
            temp = Node(item)
            self.head = temp
            self.head.next = self.head
            return
        
        temp = Node(item, self.head)
        current = self.head
        while current.next != self.head: current = current.next
        self.head = temp
        current.next = self.head

    def insertAtEnd(self, item):
        if not self.head:  return self.insertAtBegin(item)
        i = self.head
        while i.next != self.head: i = i.next
        i.next = Node(item, self.head)
        
    def length(self):
        if not self.head: return 0
        i,j = self.head,0
        while i.next != self.head: j,i = j+1, i.next
        return j+1

    def removeAt(self, ind):
        if ind < 0 or ind >= self.length(): return print("INVALID Index")
        if ind == 0:
            i = self.head
            while i.next != self.head: i = i.next
            i.next = self.head.next
            self.head = self.head.next
            return

        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = self.head if i == self.length()-2 else j.next.next

    def insertAt(self, ind, item):
        if ind < 0 or ind > self.length(): return print("INVALID Index")
        if ind == self.length(): return self.insertAtEnd(item)
        if ind == 0: return self.insertAtBegin(item)

        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = Node(item,j.next)

    def print(self):
        if not self.head: return print("Linked List is empty")
        j = self.head
        while j.next != self.head:
            print(j.data, end=" => ")
            j = j.next
        print(j.data)
        
def main():
    sll = CircularSinglyLinkedList()
    sll.insertAtEnd(6)
    sll.print()
    print(sll.length())
    sll.insertAtBegin(6)
    sll.print()
    
    # sll.removeAt(0)
    sll.print()
    sll.insertAtEnd(5)
    print(sll.length())
    sll.print()
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
    sll.print()
    sll.removeAt(0)
    sll.print()
    sll.removeAt(6)
    sll.print()
    sll.removeAt(2)
    sll.print()
    sll.removeAt(2)
    sll.print()
    sll.insertAt(0, 'START')
    sll.print()
    sll.insertAtEnd('END')
    sll.print()
    sll.insertAt(5, 9)
    sll.print()
    sll.insertAt(2, 5)
    sll.print()
    print(sll.length())

if __name__ == "__main__":
    main()

