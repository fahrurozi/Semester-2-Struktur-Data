#C Count Leaf

n = int(input())
data = list(map(int,input().split()))

class Node:
    def __init__(self, angka=None):
        self.angka = angka
        self.left = None
        self.right = None

        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, angka):
        if self.root == None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.root.left = BST()
            self.root.right = BST()
        else:
            if self.root.angka > angka:
                self.root.left.insert(angka)
            else:
                self.root.right.insert(angka)

    def getSumLeaf(self):        
        if self.root is None:
            return 0
        elif self.root.left.root is not None or self.root.right.root is not None:
            return self.root.left.getSumLeaf() + self.root.right.getSumLeaf()
        else:
            return 1 + self.root.left.getSumLeaf() + self.root.right.getSumLeaf()

tree = BST()     
for i in data:
  tree.insert(i)

print(tree.getSumLeaf())