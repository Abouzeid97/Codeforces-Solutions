x = input()
x = sorted(x)
ct = 0
while x[0] == '+':
    x.remove(x[0])
    ct += 1
w = 1
while ct > 0:
    x.insert(w, '+')
    w += 2
    ct -= 1
q = ''
q = q.join(x)
print(q)
