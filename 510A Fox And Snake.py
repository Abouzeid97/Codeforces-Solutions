x, y = map(int, input().split())
f = True
r = True
for i in range(x):
    if f == True:
        print('#'*y)
    else:
        if r == True:
            w = '.'*(y-1)
            w = w + '#'
            print(w)
            r = False
        else:
            w = '.'*(y-1)
            w = '#' + w
            print(w)
            r = True
    if f == True:
        f = False
    else:
        f = True
