num=int(input())
for a in range(1,num+1):
	for b in range(num-a):
		print(' ',end='')

	if num==a:
		for c in range((num-1)*2+1):
			print('*',end='')
	elif a==1:
		print('*')
	else:
		print('*',end='')
		for d in range((a-1)*2-1):
			print(' ',end='')
		print('*')

