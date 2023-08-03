x, y, z = map(int, input().split())
max = 0
for i in range(1, z+1):
    max = max + (i*x)

if max < y:
    print(0)
else:
    max -= y
    print(max)
