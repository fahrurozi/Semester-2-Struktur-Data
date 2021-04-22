#B Height Binary Search Tree

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

    def getTinggi(self):
        if self.root is None:
            return 0
        else:
            return 1 + max(self.root.left.getTinggi() , self.root.right.getTinggi())

tree = BST()     
for i in data:
  tree.insert(i)

print(tree.getTinggi())