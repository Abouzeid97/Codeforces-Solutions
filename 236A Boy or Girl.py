s = input()
w = []
ct = 0
for i in s:
    if i not in w:
        w.append(i)
        ct += 1
if ct % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
