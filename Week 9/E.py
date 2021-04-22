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
                
    def search(self,angka):
        if self.root.angka == None:
            return False
        if self.root.angka == angka:
            return True
        
        res1 = self.root.left.search(angka)
        if res1:
            return "YA"
        res2 = self.root.right.search(angka)
        if res2 == False:
            return "TIDAK"

n = int(input())
data = list(map(int,input().split()))
angka = int(input())
tree = BST()     
for i in data:
  tree.insert(i)

print(tree.search(angka))