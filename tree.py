class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=Node(data)
        if self.root==None:
            self.root=newnode
        else:
            temp=self.root
            while(True):
                if(data<temp.data):
                    if(temp.left==None):
                        temp.left=newnode
                        break
                    else:
                        temp=temp.left
                else:
                    if(temp.right==None):
                        temp.right=newnode
                        break
                    else:
                        temp=temp.right
    def inorder(self,root):
        if root!=None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root!=None:
            print(root.data,end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        if root!=None:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end=" ")
            
                    
                
t=tree()
t.insert(50)
t.insert(100)
t.insert(75)
t.insert(5)
t.insert(3)
t.insert(12)
t.insert(7)
t.insert(110)
t.insert(107)
t.insert(2)
t.insert(4)
t.insert(117)
t.insert(116)
t.inorder(t.root)
print()
t.preorder(t.root)
print()
t.postorder(t.root)