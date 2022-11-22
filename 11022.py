num=int(input())
arr = [[0 for col in range(2)] for row in range(num)]
for a in range(num):
	arr[a]=list(map(int,input().split()))
for a in range(num):
	print('Case #'+str(a+1)+': '+str(arr[a][0])+' + '+str(arr[a][1])+' = '+str(arr[a][0]+arr[a][1]))
