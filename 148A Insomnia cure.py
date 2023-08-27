a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = int(input())
ct = 0
for i in range(1,n+1):
    if i%a == 0 or i%b == 0 or i%c == 0 or i%d == 0 :
        ct +=1
print(ct)