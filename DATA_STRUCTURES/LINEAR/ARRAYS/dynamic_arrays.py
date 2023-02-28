"""
====================== Dynamic Arrays =================
Insertion Complexity: O(n)
traversing: O(n)
searching: O(n)

Class variables:
    data: a bucket contains all items
    length: size of array
    
Methods:
__getitem__(): index operator e.g print(x[5])
__setitem__(): change value by index e.g x[5] = 55
__delitem__(): delete operator
insert(): insert into array 
pop(): remove and return last element
pop(int): remove and return given index element
print(): print the array
"""

class Array:
    def __init__(self, *arg) -> None:
        self.data = []
        self.length = 0
        for val in arg:
            self.data.append(val)
            self.length +=1
        

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        self.length-=1
        del self.data[index]
    
    def insert(self, value):
        self.data.append(value)
        self.length+=1

    def pop(self, index = None):
        self.length-=1
        if not index: return self.data.pop()
        item = self.data[index]
        self.data.pop(index)
        return item

    def print(self):
        
        print(*self.data)

def main():

    primes = Array(1,2,3,5,7)
    primes.print()
    print(primes[4] , primes.length)
    primes[4] = 11
    primes.print()
    print(primes[4])
    del primes[4]
    primes.print()
    print(primes[3], primes.length)
    primes.insert(7)
    primes.print()
    print(primes[4], primes.length)
    print(primes.pop())
    primes.insert(7)
    primes.print()
    primes.insert(7)
    primes.print()
    print(primes.pop(4), primes.length)
    primes.print()

main()

    
    