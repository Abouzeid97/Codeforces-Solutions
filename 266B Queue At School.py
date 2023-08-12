n, t = map(int, input().split())
s = input()
while t > 0:
    i = 1
    while i < n:
        if s[i] == 'G' and s[i-1] == 'B':
            s = s[:i-1] + 'G' + 'B' + s[i+1:]
            i += 1
        i += 1
    t -= 1
print(s)