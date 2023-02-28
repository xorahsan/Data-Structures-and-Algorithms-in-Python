"""
====================== Fixed Size Array =================
Insertion Complexity: O(n)
Deletion Complexity: O(1)
Assigning Complexity: O(1)
traversing: O(n)
searching: O(n)

Class variables:
    data: a bucket contains all items
    length: length of array
    size: size of array
    
Methods:
__getitem__(): index operator e.g print(x[5])
__setitem__(): change value by index e.g x[5] = 55
__str__(): string representaion of array
__itr__(): iterator object for array
insert(index, value): insert value into array at given index
pop(int): remove and return given index element

"""

class FixedSizeArray:

    def __init__(self, size):
        self.length = size
        self.data = [None] * self.length
        self.size = 0

    def insert(self, index, value):
        if index < 0 or index >= self.length: raise ValueError("Invalid Index!")
        if self.size == self.length: raise ValueError("Array is already full")
        if not self.data[self.length-1]: self.size+=1
        self.data = self.data[:index] + [value] + self.data[index:self.length-1]

    def pop(self, index):
        if index < 0 or index >= self.length: raise ValueError("Invalid Index!")
        temp = self.data[index]
        if temp: self.size-=1
        self.data[index] = None
        return temp

    def __getitem__(self,index): 
        if index < 0 or index >= self.length: raise ValueError("Invalid Index!")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length: raise ValueError("Invalid Index!")
        if not self.data[index]: self.size+=1
        self.data[index] = value

    def __str__(self): return str(self.data)

    def __repr__(self): return self.data

    def __iter__(self): return iter(self.data)

def main():
    pass
    # x = FixedSizeArray(5)
    # print(x)
    # x[0] = 2
    # print(x)
    # x[2] = 5
    # print(x)
    # x[4] = 11
    # x[4] = 11
    # print(x.size, x.length)
    # x.insert(1, 3)
    # print(x)
    # x.insert(2, 5)
    # print(x)
    # x.insert(4, 11)
    # print(x)
    # x.insert(3, 7)
    # print(x)
    # x.insert(4, 11)
    # print(x)
    # for i in x: print(i, end=" ")
    # print()
    # x.remove(3)
    # print(x)
    # x.remove(0)
    # print(x)
    # x.remove(2)
    # print(x)
    # x.remove(x.length-1)
    # print(x)
    # x.remove(1)
    # print(x)
    # for i in x: print(i, end=" ")

if __name__ == "__main__":
    main()