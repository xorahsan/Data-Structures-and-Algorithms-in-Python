
"""
=================== Regular Trees ===================
Insertion Complexity: O(1)
Deletion Complexity: O(n)
Best for Heirarchal Structures
Each and every node is tree node itself
Each tree node has three class variables:
    parent: parent of current tree node
    data: the data in current tree node
    childern: [array] array of all childern (each child is tree node itself)
Methods:
addChild(data): add child to self
getLevel(): return level self
print(): print all tree nodes in heirarchical order
print(level=1): print tree until given level
print(level='HR'): print tree of given node name
getRoot(): return main root node of tree
getParent(data): get parent node of given data (if exist)
"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
    
    def addChild(self, data):
        data.parent = self
        self.child.append(data)

    def getLevel(self):
        i,j = 0, self
        while j.parent: i,j=i+1,j.parent
        return i

    def search(self, item):
        if self.data == item: return True
        for i in self.child: 
            if i.search(item): return True
        return False

    def getRoot(self):
        if not self.parent: return self.data
        return self.parent.getRoot()

    def getParent(self, item):
        if self.child == []: return
        
        for i in self.child:
            if i.data == item: return i.parent.data
            temp = i.getParent(item)
            if temp: return temp

        if item == self.getRoot(): return "ALREADY ON ROOT NODE"


    def print(self,level_name = None,level = None):
        if not level_name and not level and level != 0: print(self.getLevel() *"    ",'->',self.data)
        if self.parent and level_name == self.parent.data: 
            print(self.getLevel() *"    ",'->',self.data)
            for i in self.child:
                i.print(self.data)
        
        if self.getLevel() == level:
            print(self.getLevel() *"    ",'->',self.data)

        if self.child:
            for i in self.child:
                i.print(level_name, level)

def main():
    
    root = Tree("CEO")
    hr, it, markt = Tree("HR"), Tree("IT"), Tree("MARKETING")

    hr.addChild(Tree("NOMAN KHAN"))
    hr.addChild(Tree("MIR JAFAR"))
    hr.addChild(Tree("FAHAD KHAN"))
    hr.addChild(Tree("YOUSUF SHEIKH"))

    it.addChild(Tree("SALMAN KHAN"))
    it.addChild(Tree("DUMBLEDORE"))
    it.addChild(Tree("ANUSHKA SHARMA"))
    it.addChild(Tree("THING"))

    markt.addChild(Tree("RON WEASLY"))
    markt.addChild(Tree("ENID"))
    markt.addChild(Tree("TYLER"))
    markt.addChild(Tree("XAVIER"))
    wednesday = Tree("WEDNESDAY")
    markt.addChild(wednesday)

    root.addChild(hr)
    root.addChild(it)
    root.addChild(markt)

    root.print()
    print("===================")
    root.print(level_name='IT')
    print("===================")
    root.print(level=1)
    print("===================")
    print(root.search("WEDNESDAY"))
    print(root.getRoot())
    print(wednesday.getRoot())
    print("===================")
    print(root.getParent("WEDNESDAY"))
    print(root.getParent("IT"))
    print(root.getParent("CEO"))



if __name__ == "__main__":
    main()