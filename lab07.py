print("###==================#1#===================###")

class KeyIndex:
    def __init__(self, a):
        self.a = a
        
        #self.k = None

    def search(self, val):
        self.arr = self.a 
        neg= False
        for i in self.arr:
            if i*(-1) == abs(i):
                neg = True
                break 
        if neg is True:
            mn = min(self.arr)
            x = -1 * mn 
            self.arr = [self.arr[i]+x for i in range(len(self.arr))]
            val = val + x
        
        mx = max(self.arr)
        self.k = [0 for i in range(mx+1)]
        for i in range(len(self.arr)):
            ind = self.arr[i]
            self.k[ind] = self.k[ind] + 1

        if self.k[val] != 0:
            return True
        else:
            return False

        # else:
        #     mn = min(self.arr)
        #     x = -1 * mn 
        #     self.arr = [self.arr[i]+x for i in range(len(self.arr))]
        #     mx = max(self.arr)
        #     self.k = [0 for i in range(mx+1)] 
        #     for i in range(len(self.arr)):
        #         ind = self.arr[i]
        #         self.k[ind] = self.k[ind] + 1

        #     if self.k[val+x] != 0:
        #         return True
        #     else:
        #         return False

            
    def sort(self):
        v = 0
        neg = False

        for i in self.a:
            if i*(-1) == abs(i):
                neg = True
                break 
        if neg is True:
            v = -1 * min(self.a)
        x = 0
        for i in range(len(self.k)):
            while (self.k[i] > 0):
                self.a[x] = i - v 
                self.k[i] = self.k[i] - 1
                x += 1

        return self.a

###==================tester===================###

arr = [5, 4, 1, 3, 2, 7, 4]
ob = KeyIndex(arr)
s = ob.search(-2)
print(s)
so = ob.sort()
print(so)
print()


print("###==================#2#===================###")

def funCal(arr):
    hash_tab =[0 for _ in range(len(arr))] 
    for i in range(len(arr)):
        con = 0 
        num = 0
        for j in arr[i]:
            if j.lower() not in "aeiou" and j not in "0123456789":
                con = con + 1 
            elif j in "0123456789":
                num = num + int(j)

        cal = (24 * con + num) % 9
        hash_tab[i] = cal 
    # print(hash_tab)
    #print(arr)
    return hash_tab


def hashTable(arr):
    tab = funCal(arr)
    hash_table =[0 for _ in range(len(arr))] 
    for ind in range(len(tab)):
        if hash_table[tab[ind]] == 0:
           hash_table[tab[ind]] =  arr[ind] 
        else:
            inx = tab[ind] + 1
            while True:
                if hash_table[inx % len(arr)] == 0:
                    hash_table[inx % len(arr)] = arr[ind] 
                    break 
                inx = inx + 1

    return hash_table
###==================tester===================###

arr = ["ST1E89B8A32", "MU1E75B8A32",  "aA1E85a8A32", "TA1E85B8A32", "cT1E89B8A32", "dU1E75B8A32", "vA1E85B8A32", "xT1E89B8A32", "yU1E75B8A32"]
h = hashTable(arr)

print(h)

