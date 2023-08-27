n = int(input())
a = []
sct = 0
ect = 0
for q in range(n):
    w = input()
    a.append(w)
for q in range(len(a)):
    if q == 0:
        s = a[q]
        sct += 1
    else:
        if a[q] == s:
            sct += 1
        else:
            e = a[q]
            ect += 1
if sct > ect:
    print(s)
else:
    print(e)