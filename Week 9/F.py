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
            if self.root.angka < angka:
                self.root.left.insert(angka)
            else:
                self.root.right.insert(angka)
                
    po = []
    def preOrder(self):
        if self.root is not None:
            ##print(self.root.angka)
            test1.append(str(self.root.angka))
            #self.po = self.po+" " +self.root.angka
            self.root.left.preOrder()
            self.root.right.preOrder()
            
    def inOrder(self):
        if self.root is not None:
            self.root.left.inOrder()
            test2.append(str(self.root.angka))
            self.root.right.inOrder()
            
    def postOrder(self):
        if self.root is not None:
            self.root.left.postOrder()
            self.root.right.postOrder()
            test3.append(str(self.root.angka))


n = int(input())
data = list(map(int,input().split()))
data = list(dict.fromkeys(data))
tree = BST()     
for i in data:
  tree.insert(i)


test1 = []
tree.preOrder()
test1 = " ".join(test1)
print(test1)
test2 = []
tree.inOrder()
test2 = " ".join(test2)
print(test2)
test3 = []
tree.postOrder()
test3 = " ".join(test3)
print(test3)
#tree.inOrder()
#tree.PostOrder()