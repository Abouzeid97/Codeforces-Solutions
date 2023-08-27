n = int(input())
ct = 0
ct += n // 100
n %= 100
ct += n // 20
n %= 20
ct += n // 10
n %= 10
ct += n // 5
n %= 5
ct += n
print(ct)
