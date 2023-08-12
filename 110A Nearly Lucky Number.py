y = input()
ct = 0
for q in y:
    if q == '4' or q == '7':
        ct += 1
if ct == 4 or ct == 7:
    print("YES")
else:
    print("NO")
