
"""
=================== Binary Search Trees ===================
Insertion Complexity: O(logn)
Deletion Complexity: O(logn)
Search Complexity: O(logn)
Best for Heirarchal Structures
Each and every node is a binary tree node itself
Each bst node has three class variables:
    left: left bst node
    data: the data in current bst node
    right: right bst node
Methods:
addNode(data): makes new bst and add it to current bst
search(): return True if value exist else false
min(): return minimum value from bst
max(): return maximum value from bst
sum(): return sum of all values
delete(data): delete given item from bst
inOrderTraversal(): print left + print root + print right
preOrderTraversal(): print root + print left + print right
postOrderTraversal(): print left + print right + print root
print(): prints the bst
"""

class BinarySearchTree:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, item):
        if self.data == item: return
        elif self.data < item:
            if not self.right: 
                self.right = BinarySearchTree(item)
                return
            else:
                return self.right.addNode(item)
        elif self.data > item:
            if not self.left:
                self.left = BinarySearchTree(item)
                return
            else:
                return self.left.addNode(item)

    def search(self, item):
        if self.data == item: return True
        elif self.data < item:
            return self.right.search(item) if self.right else False
        return self.left.search(item) if self.left else False

    def min(self):
        if self.left: return self.left.min()
        return self.data 
    
    def max(self):
        if self.right: return self.right.max()
        return self.data 

    def sum(self):
        sum = 0
        if self.left: sum+=self.left.sum()
        sum+=self.data
        if self.right: sum+=self.right.sum()
        return sum

    def delete(self, item):
        if self.data > item:
            if self.left: self.left = self.left.delete(item)
        elif self.data < item:
            if self.right: self.right = self.right.delete(item)
        else:
            if self.left is None and self.right is None: return None
            elif self.left is None: return self.right
            elif self.right is None: return self.left
            else:
                max = self.left.max()
                self.data = max
                self.left = self.left.delete(max)
        print(self.data)
        return self

    def inOrderTraversal(self):
        temp = []
        if self.left: temp += self.left.inOrderTraversal()
        temp.append(self.data)
        if self.right: temp += self.right.inOrderTraversal()
        return temp

    def preOrderTraversal(self):
        temp = []
        temp.append(self.data)
        if self.left: temp += self.left.inOrderTraversal()
        if self.right: temp += self.right.inOrderTraversal()
        return temp

    def postOrderTraversal(self):
        temp = []
        if self.left: temp += self.left.inOrderTraversal()
        if self.right: temp += self.right.inOrderTraversal()
        temp.append(self.data)
        return temp


    def print(self):
        if self.left: self.left.print()
        print(self.data, end=" ")
        if self.right: self.right.print()


def main():
    bst = BinarySearchTree(10)
    bst.addNode(5)
    bst.addNode(15)
    bst.addNode(3)
    bst.addNode(4)
    bst.addNode(1)
    bst.addNode(6)
    bst.addNode(12)
    bst.addNode(17)


    # bst.print()
    print(bst.inOrderTraversal())
    print(bst.preOrderTraversal())
    print(bst.postOrderTraversal())
    print(bst.search(75))
    print(bst.search(5))
    print(bst.min())
    print(bst.max())
    print(bst.sum())
    print("============")
    bst.delete(12)
    print(bst.inOrderTraversal())

if __name__ == "__main__":
    main()
