class Node:
 def __init__(self,data):
     self.data=data
     self.left=None
     self.right=None
class Binarytree:
     def __init__(self):
         self.root=None
     def insert(self,data):
         new_node=Node(data)
         if self.root is None:
             self.root=new_node
             return 
tree = Binarytree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
print("binary tree:")

