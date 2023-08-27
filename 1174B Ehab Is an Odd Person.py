n = int(input())
nums = list(map(int, input().split()))
 
oddCount, evenCount = 0, 0
 
for i in nums:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
        
if oddCount > 0 and evenCount > 0:
    nums.sort()
print(*nums)