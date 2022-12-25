"""
====================== Stacks =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: a list contains all items pushed in stack
    
Methods:
__getitem__(): index operator e.g print(x[5])
__setitem__(): change value by index e.g x[5] = 55
__delitem__(): delete operator
insert(): insert into array 
pop(): remove and return last element
pop(int): remove and return given index element
print(): print the array
"""

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data == []:
            return print("STACK is empty")
        return self.data.pop(0)

    def print(self):
        print(*self.data)

    def isEmpty(self):
        return True if self.data == [] else False

    def size(self):
        return len(self.data)

def main():

    s1 = Stack()
    s1.pop()
    s1.push(5)
    s1.print()
    s1.push(4)
    s1.print()
    s1.push(3)
    s1.print()
    s1.push(2)
    s1.print()
    s1.push(1)
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()

if __name__ == "__main__":
    main()