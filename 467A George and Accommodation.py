n = int(input())
l = []
ct = 0
for i in range(n):
    input_line = input()
    values = input_line.split()
    numbers = [int(value) for value in values]
    l.append(numbers)
for i in range(len(l)):
    if l[i][0] + 2 <= l[i][1]:
        ct += 1
print(ct)