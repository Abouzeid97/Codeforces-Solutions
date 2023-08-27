s = input()
n = []
i = 0
while i in range(len(s)):
    if s[i] == ".":
        n.append(0)
        i += 1
    elif s[i] == "-" and s[i+1] == ".":
        n.append(1)
        i += 2
    elif s[i] == "-" and s[i+1] == "-":
        n.append(2)
        i += 2
i = 0
for i in range(len(n)):
    print(n[i], end="")