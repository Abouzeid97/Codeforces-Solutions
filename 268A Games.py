n = int(input())
home = [0] * n
guest = [0] * n
for i in range(n):
    home[i], guest[i] = map(int, input().split())
count = 0
for i in range(n):
    for j in range(n):
        if home[i] == guest[j]:
            count += 1
print(count)