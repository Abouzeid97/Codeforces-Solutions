n = int(input())
l = []
ct = 0
max = 0
for i in range(n):
    q = int(input())
    l.append(q)
for i in range(len(l)):
    if i == 0:
        ct += 1
        value = l[i]

        continue
    if l[i] != value:
        value = l[i]
        ct += 1
print(ct)