inputNum=int(input())

def isSequence(n):
	if n<100:
		return True
	else:
		arr=list(str(n))
		if int(arr[2])-int(arr[1])==int(arr[1])-int(arr[0]):
			return True
	return False

count=0
for i in range(1,inputNum+1):
	if isSequence(i):
		count+=1

print(count)

