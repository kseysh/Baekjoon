arr=[0 for i in range(9)]
max,count=0,0
for a in range(9):
	arr[a]=int(input())
	if arr[a]>max:
		max=arr[a]
		count=a
print(max)
print(count+1)