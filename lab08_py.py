class TreeNode:
    def __init__(self, elem):
        self.elem = elem   
        self.r = None 
        self.l = None 
        
    def heightOfTree(self, n):
        
        if n is not None:
            
            left_dep = self.heightOfTree(n.l)
            right_dep = self.heightOfTree(n.r)
            
            if left_dep > right_dep:
                return left_dep + 1 
            else:
                return right_dep + 1 
            
        else:
            return 0
        
    def getlevel(self, n, val, level):
        if n == None:
            return 0 
        if n.elem == val:
            return level 
        d_level = self.getlevel(n.l, val, level+1)
        
        if d_level != 0:
            return d_level 
        d_level = self.getlevel(n.r, val, level+1)
        
        return d_level
        
    def levelOfNode(self, parent, val):
    
        return self.getlevel(parent, val, 0)
    
    def preOrder(self, parent):

        if parent:

            print(parent.elem, end = " ")
            
            self.preOrder(parent.l)
            self.preOrder(parent.r)
            
    def postOrder(self, parent):
        if parent:
            self.postOrder(parent.l)
            self.postOrder(parent.r)
            print(parent.elem, end = " ")
            
    
        
    def inOrder(self, parent):
        if parent:
            self.inOrder(parent.l)
            
            print(parent.elem, end = " ")
            
            self.inOrder(parent.r)
            
    # def twinTree(self, x, y):
    #     if x is None and y is None:
    #         return True 
    #     if x is not None and y is  not None:
    #         return ((x.elem == y.elem) and self.twinTree(x.l, y.l) and self.twinTree(x.r, y.r))
    #     return False
    
    # def xeroxTree(self, n):
    #     if n is None:
    #         return None 
        
    #     parent_copy = TreeNode(n.elem)
    #     parent_copy.l = self.xeroxTree(n.l)
    #     parent_copy.r = self.xeroxTree(n.r)
        
    #     return parent_copy
        
    def tester(self):   
        
        if __name__ == "__main__":
            
            # root1 = TreeNode("Smart Device")
            # root1.l = TreeNode("Laptop")
            # root1.r = TreeNode("SmartPhone")
            # root1.l.l = TreeNode("Mac")
            # root1.l.r = TreeNode("Surface")
            
            # root2 = TreeNode("Smart Device")
            # root2.l = TreeNode("Laptop")
            # root2.r = TreeNode("SmartPhone")
            # root2.l.l = TreeNode("Mac")
            # root2.l.r = TreeNode("Surface")
            
            # root1 = TreeNode(1)
            # root1.l = TreeNode(2)
            # root1.r = TreeNode(3)
            # root1.l.l = TreeNode(4)
            # root1.l.r = TreeNode(5)
            
            # root2 = TreeNode(1)
            # root2.l = TreeNode(2)
            # root2.r = TreeNode(3)
            # root2.l.l = TreeNode(4)
            # root2.l.r = TreeNode(5)
            
            root = TreeNode("A")
            
            root.l = TreeNode("B")
            root.l.l = TreeNode("V")
            root.l.l.l = TreeNode("H")
            
            root.l.r = TreeNode("F")
            root.l.r = TreeNode("X")
            
            root.r = TreeNode("Y")
            root.r.r = TreeNode("G")
            root.r.r.l = TreeNode("W")
            root.r.r.r = TreeNode("L")
            
            # print("\n#================# 1(Height) #================#\n")
            # height = root.heightOfTree(root)
            # print("Height of the Tree: ", height)
            
            # print("\n#================# 2(level) #================#\n")
            # n = "A"
            # level = root.levelOfNode(root, n)
            # print(f"\nLevel of {n}: ", level)
            
            
            print("\n#================# 3(Pre Order) #================#\n")

            root.preOrder(root)

            print("\n#================# 4(Post Order) #================#\n")
            root.postOrder(root)

            print("\n#================# 5(In Order) #================#\n")
            root.inOrder(root)
            

            # print("\n#================# 6(Same tree or not) #================#\n")
            # # if root1.twinTree(root1, root2):
            # #     print("two trees are exactly same")
            # # else:
            # #     print("two trees are not same")
                
                
            # print("\n#================# 7(copy tree) #================#\n")   
              
            # cy = root1.xeroxTree(root1)
            # print("\n#===== [Tree 1] =====#") 
            # root1.preOrder(root1)
            # print("\n#===== [Tree 2] =====#")
            # root1.preOrder(cy)

ob = TreeNode(None)
ob.tester()
    
    
    