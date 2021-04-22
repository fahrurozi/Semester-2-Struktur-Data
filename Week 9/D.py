#D PostOrder
#D P

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

    def preOrder(self):
        if self.root is not None:
            print(self.root.angka)
            self.root.left.preOrder()
            self.root.right.preOrder()

            
    def postOrder(self):
        if self.root is not None:
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.angka)
            

tree = BST()     
for i in data:
  tree.insert(i)


tree.postOrder()
