n = int(input())
max = 0
intram = 0
for i in range(n):
    out, ins = map(int, input().split())
    diff = ins - out
    intram += diff
    if intram > max:
        max = intram
print(max)
