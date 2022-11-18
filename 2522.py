num = int(input())
for a in range(1,num+1):
	print(' '*(num-a)+a*'*')
for b in range(1,num):
	print(' '*b+'*'*(num-b))