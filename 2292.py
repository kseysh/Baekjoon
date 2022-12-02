num=int(input())
count=0
while True:
	if (1+(count+1)*(count)*3)>=num:
		break
	count+=1
print(count+1)