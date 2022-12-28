"""
====================== Stacks =================
Insertion Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: a list contains all items pushed in stack
    
Methods:
push(): insert into top of stack
pop(): remove and return top element of stack
print(): print the stack
isEmpty(): return True if Stack is empty else return False
top(): return top element of stack
"""

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data == []:
            return print("STACK is empty")
        return self.data.pop()

    def print(self):
        print(*self.data)

    def isEmpty(self):
        return self.data == [] 

    def size(self):
        return len(self.data)

    def top(self):
        return self.data[-1]

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