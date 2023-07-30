n = int(input())
for i in range(n):
    s = input()
    if len(s) < 11:
        print(s)
    else:
        print(f'{s[0]}{len(s)-2}{s[len(s)-1]}')
