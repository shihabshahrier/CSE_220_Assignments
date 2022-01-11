# arr = [5, 4, 3, 7, 1, 2]

# i = len(arr)-1
# while i >= 0:
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp 
#     i -= 1
# print(arr)

class Node:
    def __init__(self, e, n):
        self.elem = e 
        self.next = n
        
a5 = Node(50, None)
a4 = Node(20, a5)
a3 = Node(15, a4)
a2 = Node(17, a3)
a1 = Node(10, a2)
head = a1

def boubleSort(head):
    size = 0
    n0 = head 
    while n0 is not head:
        size += 1
        n0 = n0.next
        
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

    return head
    
#tester     


s = boubleSort(head)

node = s
while node != None:
    if node.next == None:
        print(node.elem, end = "")
    else:
        print(node.elem, end = " -> ")
    node = node.next

    