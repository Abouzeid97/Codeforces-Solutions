s = input()
capct = 0
smct = 0
for q in s:
    if q.isupper() == True:
        capct += 1
    else:
        smct +=1

if capct <= smct:
    s = s.lower()
else:
    s = s.upper()
print(s)