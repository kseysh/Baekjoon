mon,day=map(int,input().split())
arr=[31,28,31,30,31,30,31,31,30,31,30,31]
totalday=0
for a in range(mon-1):
	totalday+=arr[a]

totalday+=day

if totalday%7==0:
	print('SUN')
elif totalday%7==1:
	print('MON')
elif totalday%7==2:
	print('TUE')
elif totalday%7==3:
	print('WED')
elif totalday%7==4:
	print('THU')
elif totalday%7==5:
	print('FRI')
elif totalday%7==6:
	print('SAT')

#요일을 배열을 사용하여 풀었다면 좀 더 간결하였을 것