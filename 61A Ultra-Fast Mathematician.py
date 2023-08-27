a = input()
b = input()
c = ""
for q, s in zip(a, b):
    w = int(q) ^ int(s)
    c += str(w)
print(c)