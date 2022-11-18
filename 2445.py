num=int(input())
for a in range(1,num+1):
	print('*'*a+' '*(num-a)*2+'*'*a)
for b in range(1,num):
	print('*'*(num-b)+' '*2*b+'*'*(num-b))