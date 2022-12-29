
"""
======================= Circular Doubly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Node class Variables:
    value: value of current node
    next: whole next Node

Singly Linked List class variables:
    head: the whole node of current singly linked list head


Singly Linked List Methods:

insertAtBegin(data) # insert Node at start

printAll() # print every element of current linked list

length() # return length of current Linked List

insertAtEnd(data) # insert Node at end

insertAt(index, data) # insert Node at the given index

removeAt(index) #remove Node by Index

find(data) #return index of first occurence of given value

"""

class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, item):
        if not self.head:
            temp = Node(item)
            self.head = temp
            self.head.next = self.head
            self.head.prev = self.head
            return
        
        current = self.head
        while current.next != self.head: current = current.next
        temp = Node(item, self.head, current)
        current.next = temp
        self.head.prev = temp
        self.head = temp

    def insertAtEnd(self, item):
        if not self.head:  return self.insertAtBegin(item)
        i = self.head
        while i.next != self.head: i = i.next
        i.next = Node(item, self.head,i)
        self.head.prev = i.next
        
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
            self.head.prev = i
            return
        elif ind == self.length()-1:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
            return

        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = j.next.next
        j.next.prev = j

    def insertAt(self, ind, item):
        if ind < 0 or ind > self.length(): return print("INVALID Index")
        if ind == self.length(): return self.insertAtEnd(item)
        if ind == 0: return self.insertAtBegin(item)
        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        temp = Node(item,j.next,j)
        j.next.prev = temp
        j.next = temp
        

    def print(self, reverse = False):
        if not self.head: return print("Linked List is empty")
        i = self.head
        while i.next != self.head:
            if not reverse: print(i.data, end=" => ")
            i = i.next
        if not reverse: return print(i.data)
        current = self.head.prev
        while current != self.head:
            print(current.data, end=" => ")
            current = current.prev
        print(current.data)
        
def main():
    sll = CircularDoublyLinkedList()
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
    sll.print(reverse=True)
    sll.insertAt(5, 9)
    sll.print()
    sll.insertAt(2, 5)
    sll.print()
    sll.print(reverse=True)

    print(sll.length())

if __name__ == "__main__":
    main()

