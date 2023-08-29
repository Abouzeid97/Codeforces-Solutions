m = 240
x,y = map(int,input().split())
j = 0
t= 0
i = 0
b = False
while i != x+1 :
    t += i*5
    if t + y > m:
        j = i-1
        b= True
        break
    if t + y == m:
        j = i
        b = True
        break
    i+=1 
if b == True:
    print(j)
else:
    print(x)