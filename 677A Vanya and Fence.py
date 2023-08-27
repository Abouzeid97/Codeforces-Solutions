n, t = map(int, input().split())
l = list(map(int, input().split()))
ct = 0

for i in range(len(l)):
    if l[i]/t % 1 != 0:
        x = int(l[i]/t) + 1
    else:
        x = l[i]/t
    ct += x
print(int(ct))