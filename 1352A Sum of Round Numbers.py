t = int(input())  
for _ in range(t):  
    n = int(input())  
    roundNums = []  
    power = 1      
    while n > 0:
        digit = n % 10  
        
        if digit != 0:
            roundNums.append(str(digit * power))
        
        n //= 10  
        power *= 10     
    print(len(roundNums))  
    print(' '.join(roundNums)) 