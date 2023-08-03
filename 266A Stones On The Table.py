n = int(input())
s = input()
i = 0
j = 1
ct = 0
while j + 1 <= n:
    if s[i] == s[j]:
        ct+=1
    j+=1
    i+=1
print(ct)