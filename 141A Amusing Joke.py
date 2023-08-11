s = input()
n = input()
q = input()
w = s + n
w = sorted(w)
q = sorted(q)
if w == q  :
    print("YES")
else:
    print("NO")