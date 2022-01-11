class Node:
    def __init__(self, data):
        self.elem=data
        self.left=None
        self.right=None
        self.parent=None
        
def createTree(a, i):
    if i < 0 or i >= len(a) or a[i] == None:
        return None 
    
    else:
        root = Node(a[i])
        root.left = createTree(a, 2*i)
        root.right = createTree(a, (2*i) + 1)
        
        if root.left != None:
            root.left.parent = root 
            
        if root.right != None:
            root.right.parent = root 
    
    return root

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.elem,end=" ")
        inOrder(root.right)
        
def preOrder(root):
    if root != None:
        print(root.elem,end=" ")
        inOrder(root.left)
        inOrder(root.right)

def postOrder(root):
    if root != None:
        inOrder(root.left)
        inOrder(root.right)
        print(root.elem,end=" ")


if __name__ == '__main__':
    
    arr = [None,"A","B","Y","V","E",None,"G","H",None,None,"X",None,None,"W","L"]

    root = createTree(arr, 1)

 
    preOrder(root)
    print()
    postOrder(root)
    inOrder(root)  
    print() 