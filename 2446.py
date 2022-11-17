num=int(input())
for a in range(0,num):
	print(' '*a+'*'*(2*(num-a)-1))
for b in range(2,num+1):
	print(' '*(num-b)+'*'*(2*b-1))