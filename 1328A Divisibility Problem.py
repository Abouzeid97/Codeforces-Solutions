def solve():
    a,b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)
        
for _ in range(int(input())):
    solve()