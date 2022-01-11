##=======================# 1 #=======================##

def mInd(x, y, z):
    if y == z:
        return y
    
    ind = mInd(x, y+1, z)
    
    if x[y] < x[ind]:
        return y 
    else:
        return ind 

    
def reSeSort(x, n, ind):
    if ind == n:
        return -1 
    
    inx = mInd(x, ind, n-1)
    
    if inx != ind:
        temp = x[ind]
        x[ind]= x[inx]
        x[inx] = temp
        
    reSeSort(x, n, ind + 1)

#tester 
arr = [4, 3, 1, 5, 2, 0, 7]
n = len(arr)

reSeSort(arr, n, 0) 

for i in arr:
    print(i, end = " ")

##=======================# 2 #=======================##
print()
def inSortRec(a, n):
    if n <= 1:
        return 
    
    inSortRec(a, n-1)
    l = a[n-1]
    z = n - 2
    
    while (z >= 0 and a[z]>l):
        a[z+1] = a[z]
        z = z-1 
    a[z+1] = l 

#tester 
arr = [4, 3, 1, 5, 2, 0, 7]
n = len(arr)

inSortRec(arr, n) 

for i in arr:
    print(i, end = " ")

##=======================# 3 #=======================##
print()

class Node:
    def __init__(self, e, n):
        self.elem = e 
        self.next = n

def boubleSort(head):
    size = 0
    n = head 
    while n is not head:
        size += 1
        n = n.next
    for i in range(size-1):
        on = head 
        n = on.next 
        back = None 
        while n:
            if on.elem > n.elem: 
                if back == None: 
                    back = on.next 
                    n = n.next 
                    back.next = on 
                    on.next = n 
                    head = back 
                else: 
                    tempo = n 
                    n = n.next 
                    back.next = on.next 
                    back = tempo 
                    tempo.next = on 
                    on.next = n 
            else:
                back = on 
                on = n 
                n = n.next 
        i = i + 1
        head = on
    return head
    
#tester     
a5 = Node(50, None)
a4 = Node(20, a5)
a3 = Node(25, a4)
a2 = Node(12, a3)
a1 = Node(10, a2)
head = a1

s = boubleSort(head)

node = s
while node != None:
    if node.next == None:
        print(node.elem, end = "")
    else:
        print(node.elem, end = " -> ")
    node = node.next

##=======================# 4 #=======================##
print()

class Node:
    def __init__(self, e, n):
        self.elem = e 
        self.next = n

def selSort(head):
    n = head 
    
    while n:
        t = n 
        tn = n.next 
        
        while tn:
            if t.elem > tn.elem:
                t = tn 
            tn = tn.next 
        m = n.elem
        n.elem = t.elem
        t.elem = m 
        n = n.next
    return head 

#tester         
a5 = Node(47, None)
a4 = Node(25, a5)
a3 = Node(21, a4)
a2 = Node(9, a3)
a1 = Node(10, a2)
a0 = Node(5, a1)
head = a0

s = selSort(head)
node = s
while node != None:
    if node.next == None:
        print(node.elem, end = "")
    else:
        print(node.elem, end = " -> ")
    node = node.next
        


##=======================# 5 #=======================##
print()

class Node:
    def __init__(self, e, n):
        self.elem = e 
        self.next = n
        self.prev = None

def sI(h, n):
    on = None 
    if h == None:
        h = n
    elif h.elem >= n.elem:
        n.next = h 
        n.next.prev = n 
        h = n 
    else:
        on = h 
        
        while on.next != None and on.next.elem <n.elem:
            on = on.next 
            
        n.next = on.next 
        
        if on.next != None:
            n.next.prev = n 
        
        on.next = n 
        n.prev = on 
    return h

def  inSort(head):
    s = None 
    n = head 
    while n!= None:
        nxt = n.next 
        n.prev = None 
        n.next =None 
        s = sI(s, n)
        n = nxt 
    head = s 
    return head

#tester 
a5 = Node(50, None)
a4 = Node(25, a5)
a3 = Node(20, a4)
a2 = Node(30, a3)
a1 = Node(10, a2)
a1.prev = None
a2.prev = a1
a3.prev = a2
a4.prev = a3
a5.prev = a4
head = a1


iS = inSort(head)
node = iS
while node != None:
    if node.next == None:
        print(node.elem, end = "")
    else:
        print(node.elem, end = " -> ")
    node = node.next

##=======================# 6 #=======================##
print()

def biSearch(a, l, h, n):
    if h >= l:
        m = l+(h-l)//2 
        
        if a[m] == n:
            return m 
        
        elif a[m] > n:
            return biSearch(a, l, m-1, n)
        
        else:
            return biSearch(a, m+1, h, n)
    else:
        return -1 

#tester     
arr = [2, 3, 5, 7, 8, 10]
n = 8 

r = biSearch(arr, 0, len(arr)-1, n)

if r != -1:
    print(r)
else:
    print("No such value")
    
##=======================# 7 #=======================##
print()

arr = [0 for i in range(2000)]

def fibonacci(n):
    if n <= 1:
        return n 
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fibonacci(n-1) + fibonacci(n-2)
        return arr[n]
    
#tester   
n = 1900
nf = fibonacci(n)
print(nf)