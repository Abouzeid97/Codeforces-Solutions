n = int(input())
ct = 0
for q in range(0, n):
    x, y, z = map(int, input().split())
    if x + y + z > 1:
        ct += 1
print(ct)
