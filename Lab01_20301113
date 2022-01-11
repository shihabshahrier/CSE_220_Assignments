#============##============#
# Assignment 01
#============##============#

# Name : Shiahb Shahriear Antor
# ID : 20301113
# SEC: 07

#============##============#



#=======# problem 01 #=======#


def shiftLeft(source, k):
    i = 0
    while i < len(source):
        if i < len(source)-k:
            source[i]= source[k+i] 
        else:
            source[i] = 0
            
        i += 1
        
    print(source)   
       
      
source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)


#=======# problem 02 #=======#


def rotateLeft(source,k):
    i = 0
    while i < len(source) - k:
        temp = source[i]
        source[i] = source[k+i]
        source[k+i] = temp
        i += 1
    print(source)
    
source=[10, 20, 30, 40, 50, 60]   
rotateLeft(source,3)


#=======# problem 03 #=======#


def remove(source, size, idx):
    i = idx
    while i < size:
        source[i] = source[i+1]
        i += 1
    print(source)
    
source=[10,20,30,40,50, 0,0]  
remove(source,5,2)


#=======# problem 04 #=======#


def removeAll( source, size, element):
    for i in range(size):
        if source[i] == element:
            source[i] = 0
    for j in range(size):
        if source[j] == 0:
            k = j
            while k < size:
                if source[k] != 0:
                    source[j] = source[k]
                    source[k] = 0
                    break
                k += 1
    print(source)

source=[10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source,7,2)


#=======# problem 05 #=======#


def weightDistro(arr):
    sum1 = 0
    judge = False
    for i in range(len(arr)):
        sum1 = sum1 + arr[i]
        sum2 = 0
        for j in range(i+1, len(arr)):
            sum2 = sum2 + arr[j]
        if sum1 == sum2:
            judge = True
            break
    print(judge)
        
arr = [10, 3, 1, 2, 10]
weightDistro(arr)


#=======# problem 06 #=======#


def arraySeries(n):
    n_list = [0 for _ in range(n*n)]
    x = n-1
    for i in range(0, len(n_list), n):
        for k in range(n-x):
            n_list[i + (n - 1 - k)] =  k+1  
        x = x-1  
    print(n_list)

n = 4
arraySeries(n)


#=======# problem 07 #=======#


def maxBouchCount(arr):
    l = len(arr)
    max_val = 0
    for i in range(l):
        count = 1
        for j in range(i+1, l):
            if arr[i] == arr[j]:
                count = count + 1
            else:
                break  
        if count > max_val:
            max_val = count
    print(max_val)

arr = [1,1,2, 2, 1, 1,1,1]
maxBouchCount(arr)


#=======# problem 08 #=======#


def printRepeating(arr):
    arr2 = list(set(arr))
    arr3 = []
    judge = False
    for i in range (len(arr2)):
        count = 0
        for j in range (len(arr)):
            if arr2[i] == arr[j]:
                count = count + 1
        arr3.append(count)
        
    for i in range (0, len(arr3)-1):
        for j in range (i + 1, len(arr3)):
            if arr3[i] != 1:
                if arr3[i] == arr3[j]:
                    judge = True
                    break
                
    print(judge)
                

arr = [4,5,6,6,4,3,6,4]
printRepeating(arr)



#=======##=======# Cicular Array #=======##=======#


#=======# problem 01 #=======#


def palindrome(arr, start, size):
    s = start
    last = (start + size-1)%len(arr)
    count = 0
    for i in range(size//2):
        if arr[s+i] == arr[last-i]:
            count += 1
        else:
            pass

    if count == size//2:
        print("Palindrome")
    else:
        print("Not palindrome")

arr = [20,10,0,0,0,10,20,30]
palindrome(arr, 5, 5) 


#=======# problem 02 #=======#


def returnLinear(arr1, arr2, start1, start2, size1, size2):
    s1 = start1
    
    arr3 = []
    for i in range(size1):
        x = arr1[s1]
        s2 = start2
        for j in range(size2):
            y = arr2[s2]
            # print(f"{x} -> {y}")
            if y == x:
                arr3.append(x)
            else:
                pass
            s2 = (s2 + 1)%len(arr2)
            
        s1 = (s1 + 1)%len(arr1)
    print(arr3)
    
arr1 = [40,50,0,0,0,10,20,30]
arr2 = [10,20,5,0,0,0,0,0,5,40,15,25]

returnLinear(arr1, arr2, 5, 8, 5, 7)


#=======# problem 03 #=======#


import random as ran

def musicalChair(arr, size):

    while size > 1:
        music = ran.randint(0, 3)
        
        for i in range(len(arr)-1):
            temp = arr[0]
            arr[0] = arr[i+1]
            arr[i+1] = temp

        if music == 1:
            print(f"(x) {arr[size//2]} is Eliminated!")

            remove = size//2 
            for i in range(remove, size - 1):
                arr[i] = arr[i+1]
            arr[size-1] = 0
            size -= 1
            new_arr = [0 for _ in range(size)]

            for i in range(size):
                new_arr[i] = arr[i]
            arr = new_arr
    print("#================######==================#\n")
            
    print(f"* {arr[0]} is the Winner *")
    
    print("\n#================######==================#")
        
        
arr = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7"]
musicalChair(arr, 7)








