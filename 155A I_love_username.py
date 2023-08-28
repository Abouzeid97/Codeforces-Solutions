n = int(input())
l = list(map(int, input().split()))
min = l[0]
max = l[0]
ct = 0
for i in range(len(l)):
    if l[i] > max :
        ct+=1
        max = l[i]
    if l[i] < min:
        ct += 1
        min = l[i]
print(ct)
