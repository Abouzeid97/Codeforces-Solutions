n = int(input())
s = input().upper()
dct = 0
act = 0
if n == len(s):
    for q in s:
        if q == 'D':
            dct += 1
        else:
            act += 1
    if dct > act:
        print("Danik")
    elif dct < act:
        print("Anton")
    else:
        print("Friendship")
