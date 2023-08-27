def equilibrium(l):
	x_sum = 0
	y_sum = 0
	z_sum = 0
	for l1 in l:
		x_sum += l1[0]
		y_sum += l1[1]
		z_sum += l1[2]
	if(x_sum == 0 and y_sum == 0 and z_sum == 0):
		print("YES")
	else:
		print("NO")
 
 
n = int(input())
l = []
for i in range(n):
	l1 = list(map(int,input().strip().split()))
	l.append(l1)
equilibrium(l)