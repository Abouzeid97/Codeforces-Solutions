n = int(input())
l = list(map(int, input().split()))
max = 0
for i in range(n):
    max += l[i]
max = max / n
print(max)