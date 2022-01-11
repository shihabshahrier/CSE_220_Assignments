def printR(s, i, c):
    if i == len(s):
        print(f"count is {c}", end=" ") 
    else:
        # if i < len(s):
        #     printR(s, i + 1, c)
        #     if 57 >= ord(s[i]) >= 48 and ord(s[i])%2 != 0:   
        #         print(s[i], end = " ")
        #         c = c + 1
        d = s[i].isdigit()
        if d:
            if int(s[i])%2 != 0:
                c += 1 
            else:
                d = False 
                
        i+=1 
        printR(s, i, c)
        if d:
            print(s[i-1], end = "")

            
s = "Axy3*8g572961" 
x = printR(s, 0, 0)
