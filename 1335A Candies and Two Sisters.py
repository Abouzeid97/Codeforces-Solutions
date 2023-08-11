t = int(input())
l = []
for q in range(0,t):
    n= int(input())
    ct = 0
    if n > 2:
        if n % 2 != 0:
            ct = n // 2
            
        else:
            ct = int((n/2) -1) 
        l.append(ct)
    else:
        l.append(0)
for q in range(len(l)):
    print(l[q])