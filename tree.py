class TreeNode:
    def __init__(self, elem):
        self.data = elem   
        self.children = []
        self.parent = None 
    
    def getLevel(self):
        level = 0
        p = self.parent 
        while p:
            level += 1
            p = p.parent
            
        return level 
    
    def addChild(self, child):
        child.parent = self 
        self.children.append(child)
    
    def pre(self):
        space = " " * self.getLevel()*4
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for c in self.children:
                c.pre()
                
    def post(self):
        space = " " * self.getLevel()*4
        prefix = space + u"|\u0305  " if self.parent else ""
        if self.children:
            for c in self.children:
                c.post()
        print(prefix + self.data)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("ROG"))

    smartphone = TreeNode("Smartphone") 
    smartphone.addChild(TreeNode("iPhone"))
    smartphone.addChild(TreeNode("Samsang"))
    smartphone.addChild(TreeNode("MI"))
    smartphone.addChild(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("LG"))
    tv.addChild(TreeNode("Sony"))

    root.addChild(laptop)
    root.addChild(smartphone)
    root.addChild(tv)

    #root.printTree()
    return root 

if __name__ == "__main__":
    root = build_product_tree()
    root.pre() 
    print("\n\n")
    root.post() 
    print(root.getLevel())
