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
            return -1
        
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
        return self.getlevel(parent, val, 1)
    
    
    def preOrder(self, parent, root):
        if parent:
            l = self.levelOfNode(root, parent.elem) - 1
            space = " " * l*4
            prefix = space + "|__" if l != 0 else u"\u6839"
            
            print(prefix, parent.elem)

            self.preOrder(parent.l, root)
            self.preOrder(parent.r, root)
            
            
    def postOrder(self, parent, root):
        if parent:
            l = self.levelOfNode(root, parent.elem) - 1
            space = " " * l*4
            prefix = space + u"|\u0305\u0305 " if l != 0 else u"\u6839"   
            
            self.postOrder(parent.l, root)
            self.postOrder(parent.r, root)
            print(prefix, parent.elem)

    
        
    def inOrder(self, parent, root):
        if parent:
            l = self.levelOfNode(root, parent.elem)-1
            space = " " * l*4
            prefix = space + "|--> " if l != 0 else u"\u6839"  

            self.inOrder(parent.l, root)
            print(prefix, parent.elem)

            self.inOrder(parent.r, root)
            
    def twinTree(self, x, y):
        if x is None and y is None:
            return True 
        if x is not None and y is  not None:
            return ((x.elem == y.elem) and self.twinTree(x.l, y.l) and self.twinTree(x.r, y.r))
        return False
    
    def xeroxTree(self, n):
        if n is None:
            return None 
        
        parent_copy = TreeNode(n.elem)
        parent_copy.l = self.xeroxTree(n.l)
        parent_copy.r = self.xeroxTree(n.r)
        
        return parent_copy
        
    def tester(self):   
        
        #Tree 1   
        root1 = TreeNode("Anime")
        
        root1.l = TreeNode("Shounen")
        root1.l.l = TreeNode("DRAGON BALL")
        root1.l.r = TreeNode("Naruto")
        
        root1.r = TreeNode("Thriller")
        root1.r.l = TreeNode("Death Note")
        root1.r.r = TreeNode("PSYCHO-PASS")
                
        #Tree 2
        root2 = TreeNode("Anime")
        
        root2.l = TreeNode("Shounen")
        root2.l.l = TreeNode("DRAGON BALL")
        root2.l.r = TreeNode("Naruto")
        
        root2.r = TreeNode("Thriller")
        
        print("\n#================# 1(Height) #================#\n")
        height = root1.heightOfTree(root1)
        print("Height of the Tree: ", height)
        
        print("\n#================# 2(level) #================#\n")
        n = "Shounen"
        level = root1.levelOfNode(root1, n)
        print(f"Level of '{n}': ", level)
               
        print("\n#================# 3(Pre Order) #================#\n")

        root1.preOrder(root1, root1)

        print("\n#================# 4(Post Order) #================#\n")
        root1.postOrder(root1, root1)

        print("\n#================# 5(In Order) #================#\n")
        root1.inOrder(root1, root1)
        
        print("\n#================# 6(Same tree or not) #================#\n")
        print("#case01\n")
        
        #Case 01
        xerox1 = root1.twinTree(root1, root2)
        if xerox1:
            print(u"    \u2713 Two trees are exactly same")
        else:
            print(u"    \u2717 Two trees are not same")
        
        print("\n#case02\n")
        #Tree 2 Extention
        root2.r.l = TreeNode("Death Note")
        root2.r.r = TreeNode("PSYCHO-PASS")  
        
        #Case 02
        xerox2 = root1.twinTree(root1, root2)
        if xerox2:
            print(u"    \u2713 Two trees are exactly same")
        else:
            print(u"    \u2717 Two trees are not same")
         
        print("\n#================# 7(copy tree) #================#\n")   
          
        cy = root1.xeroxTree(root1)
        print("\n#===== [Original Tree] =====#\n") 
        root1.preOrder(root1, root1)
        print("\n#===== [Clone Tree] =====#\n")
        root1.preOrder(cy, cy)
        print("\n#===== [ End ] =====#\n")   

#================# Problem (1 -> 7) #================# 
ob = TreeNode(None)
ob.tester()

#================# #================# 



    