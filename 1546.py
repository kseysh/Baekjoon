maxval=0
num=int(input())
arr=list(map(int,input().split()))
maxval=max(arr)
for j in range(num):
	arr[j]=(arr[j]/maxval)*100
sum=sum(arr)
print(sum/num)