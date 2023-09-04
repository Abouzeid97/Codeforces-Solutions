r, b = map(int, input().split())
ct = 0
while  b != 0 and r != 0:
    r-=1
    b-=1
    ct +=1

if r > 1 :
    temp =  r  / 2 
if b > 1 :
    temp = b / 2

print(f"{ct} {int(temp)}")