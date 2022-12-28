"""
======================= Doubly Linked List ======================

Traversal Time Complexity: O(n)
Insertion/Deletion Time Complexity at start: O(1)
Insertion Time Complexity: O(n)
Deletion Time Complexity: O(n)

Node class Variables:
    value: value of current node
    next: whole next node
    prev: whole previous node


Doubly Linked List class variables:
    head: the whole node of current doubly linked list head


Doubly Linked List Methods:

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
    def __init__(self, data = None, next = None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, item):
        temp = Node(item, self.head)
        if self.head: self.head.prev = temp
        self.head = temp

    def insertAtEnd(self, item):
        if not self.head:  return self.insertAtBegin(item)
        i = self.head
        while i.next: i = i.next
        i.next = Node(item,None,i)
        
    def length(self):
        i, j = 0,self.head
        while j: i,j = i+1,j.next
        return i

    def removeAt(self, ind):
        if ind < 0 or ind >= self.length(): return print("INVALID Index")
        if ind == 0:
            self.head.next.prev = None
            self.head = self.head.next
            return
        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = None if i == self.length()-2 else j.next.next
        j.next.prev = j

    def insertAt(self, ind, item):
        if ind < 0 or ind > self.length(): return print("INVALID Index")
        if ind == self.length(): return self.insertAtEnd(item)
        if ind == 0: return self.insertAtBegin(item)

        i,j = 0,self.head
        while i < ind-1: i,j = i+1,j.next
        j.next = Node(item,None,j) if not j.next else Node(item,j.next,j)

    def find(self, item):
        i,j = 0,self.head
        while i < self.length():
            if j.data == item: return i
            i,j=i+1,j.next
        return -1


    def print(self, reverse = False):
        
        if not self.head: return print("Linked List is empty")
        i = self.head
        while i.next:
            if not reverse: print(i.data, end=" => ")
            i = i.next
        if not reverse: return print(i.data)
        while i.prev:
            print(i.data, end=" => ")
            i = i.prev
        print(i.data)

        
def main():
    sll = SinglyLinkedList()
    sll.insertAtEnd(6)
    sll.print()
    sll.print(reverse=True)
    print(sll.length())
    sll.insertAtBegin(6)
    sll.print()
    sll.print(reverse=True)
    sll.removeAt(0)
    sll.print(reverse=True)
    sll.print()
    sll.insertAtEnd(5)
    print(sll.length())
    sll.insertAtBegin(4)
    sll.print()
    sll.print(reverse=True)
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
    sll.print(reverse=True)
    print(sll.length())
    sll.removeAt(0)
    sll.print()
    sll.insertAt(6, 0)
    sll.print()
    sll.print(reverse=True)
    print(sll.find(9))


if __name__ == "__main__":
    main()

