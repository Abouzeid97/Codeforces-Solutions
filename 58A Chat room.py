s = input()
q = "hello"
g = []
i = 0
t = False
for w in s:
    if w == q[i]:
        g.append(w)
        i += 1
        if i == len(q):
            print("YES")
            t = True
            break
if t == False:
    print("NO")