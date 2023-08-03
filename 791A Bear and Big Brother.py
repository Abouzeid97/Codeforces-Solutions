x, y = map(int, input().split())
ct = 0
while x <= y:
    x *= 3
    y *= 2
    ct += 1
print(ct)
