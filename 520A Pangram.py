n = int(input())
s = input()
s = set(s.lower())
q = set('abcdefghijklmnopqrstuvwxyz')
if s == q:
    print('YES')
else:
    print('NO')