x = int (input())
w = 0
ct = 0
while True:
    if w < x:
        w+= 5 
        ct += 1 
    else:
        break
print(ct)