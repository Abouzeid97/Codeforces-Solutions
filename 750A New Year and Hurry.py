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

#######################################
#### simple algorithm #####

n, k = map(int, input().split())
sum = 0
i = 1

while i <= n and sum + 5*i <= (240 - k):
    sum += 5*i
    i += 1
print(i - 1)
