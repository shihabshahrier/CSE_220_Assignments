class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
        
def insertLevelOrder(arr, root, i, n):
    if i<0 or i>=len(arr) or arr[i]==None:
        return None
    if i < n:
        temp = newNode(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i , n)
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 1, n)
    return root

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end="->")
        inOrder(root.right)
def preOrder(root):
    if root!=None:
        print(root.data,end="->")
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end="->")
        
if __name__ == '__main__':
    arr = [None,"A","B","Y","V","E",None,"G","H",None,None,"X",None,None,"W","L"]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 1, n)
    print("pre-order:")
    preOrder(root)
    print()
    print("post-order:")
    postOrder(root)
    print()
    print("In-order:")
    inOrder(root)