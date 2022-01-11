##================ #1(a) ==================##
def fact(n):
    if n > 1:
        return (n*fact(n-1))
    else:
        return 1
    
f = fact(6)

print(f) 

##================ #1(b) ==================##

def fib(n, s, ne):
    if n-1 == 0:
        return ne
    if n > 0:
        temp = ne
      
        ne = s + ne
        
        return fib(n-1,temp, ne)
    
f = fib(5, 0, 1)

print(f)

##================ #1(c) ==================##

def revArr(arr, s, l):
    if s <= l:
        temp = arr[s]
        arr[s]= arr[l]
        arr[l] = temp 
        return revArr(arr, s+1, l-1)
    
    else:
        return arr
    
arr = [5, 6, 7, 8, 9]
r = revArr(arr, 0, 4)
print(r)

##================ 1 (d) ==================##

def powerN(num, p):
    if p > 0:
        return num * powerN(num, p-1)
    else:
        return 1
    
p = powerN(5, 3)
print(p)

##================ #2(a) ==================##

def dtoB(d):
    if d == 0:
        return 0
    else:
        return (d % 2 + 10 * dtoB(int(d // 2)))
    
b = dtoB(10)
print(b)

##================ #2(b) ==================##

class Node:
    def __init__(self, e, n):
        self.elem = e 
        self.next = n

a7 = Node(70, None)
a6 = Node(60, a7)
a5 = Node(50, a6)
a4 = Node(40, a5)
a3 = Node(30, a4)
a2 = Node(20, a3)
head = Node(15, a2)



def sumList(head):
    n = head
    if n == None:
        return 0
    else:
        return n.elem + sumList(n.next)
n = head
s = sumList(n)
print(s)

##================ #2(c) ==================##


def revList(head):
    if head == None:
        return 
    if head.next == None:
        return head 
    n = revList(head.next) 
    head.next.next = head 
    head.next = None 
    return n 

def printL(r):
    if r == None:
        return 
    elif r.next == None:
        print(r.elem, end = "")
    else:
        print(r.elem, end = " -> ")
        printL(r.next)
    
r = revList(head)
printL(r)
print()
##================ #3 ==================##

def hocBuilder(height):
    if height == 0:
        return 
    elif height == 1:
        return 8 
    else:
        return 5 + hocBuilder(height-1)
    
b = hocBuilder(4)
print(b)


##================ #4(a) ==================##

def printN(num):
    if num == 0:
        return
    printN(num - 1)
    print(num, end = " ")
    
def pat(n, i):
    if n == 0:
        return 
    printN(i)
    print("\n", end = "")
    pat(n - 1, i + 1)
n= 5 
pat(n, 1)

##================ #4(b) ==================##

def space(s):
    if s == 0:
        return
    print(" ", end = " ")
    space(s-1)

def number(nu):
    if nu == 0:
        return 
    number(nu-1)
    print(nu, end = " ")
    
def pat(x, y):
    if x == 0 :
        return 
    
    space(x-1)
    number(y - x + 1 )
    print()
    pat(x-1, y)
    
x = 5 

pat(x, x)

##================ #5 ==================##

class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])
            print(str(idx+1) + ". Investment: " + str(array[idx]) + "; Profit: " + str(profit))
            self.print(array, idx+1)
            
    def calcProfit(self,investment):
        if investment <= 25000:
            return 0.0
        else:
            value = investment - 100000
            value = value / 100
            value = value + value + value + value + value + value + value + value
            return value + 3375.0
        

array = [25000,100000,250000,350000]
f = FinalQ()
f.print(array, 0)


