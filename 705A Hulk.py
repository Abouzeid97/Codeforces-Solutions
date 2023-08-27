n = int(input())
a = "I hate "
b = "that I love "
c = "that I hate "
if n == 1:
    print("I hate it")
else:
    for i in range(n):
        if i == 0:
            continue
        if i % 2 != 0:
            a += b
        else:
            a += c
    a += "it"
    print(a)