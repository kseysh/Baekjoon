num=int(input())
b=1
for a in range(1,num+1):
	for b in range(num-a):
		print(' ',end='')
	for c in range(a):
		print('*', end=' ')
	print()