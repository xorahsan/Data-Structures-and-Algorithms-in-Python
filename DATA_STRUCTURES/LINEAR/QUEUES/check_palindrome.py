# Problem: Check Palindrome using Queue

import queues
Queue = queues.Queue


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
    palindrome = "tattarrattat"
    q,st = Queue(),Stack()
    for i in palindrome:
        q.enQueue(i)
        st.push(i)

    flag = True
    for i in palindrome:
        _q,_s = q.deQueue(), st.pop()
        if _q != _s:
            flag = False
            break
    print("YES") if flag else print("NO")

main()
