n = int(input())
l = []
ct = 0
for i in range(n):
    s = input()
    l.append(s)
for i in range(n):
    if '++' in l[i]:
        ct+=1
    if '--' in l[i]:
        ct-=1
print(ct)