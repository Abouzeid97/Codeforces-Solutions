l = list(map(int, input().split()))
l.sort(reverse=True)
q = l[0] - l[1]
q += l[1] - l[2]
print(q)