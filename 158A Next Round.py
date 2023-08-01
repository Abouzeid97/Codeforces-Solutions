n,k = map(int, input().split())
l = list(map(int , input().split()))
ct = 0

for i in range(len(l)):
    if l[i] > 0 and l[i] >= l[k-1]:
        ct+=1
print(ct)