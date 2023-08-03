x, n = map(int, input().split())

for i in range(n):
    if x % 10 != 0:
        x -= 1
    else:
        x /= 10
print(int(x))
