num = int(input())
arr=list(map(int,input().split()))

maxval=arr[0]
minval=arr[0]
for a in arr:
	maxval=a if a>maxval else maxval
	minval=a if a<=minval else minval
print(minval,maxval,end=' ')

#다른 방식으로도 풀어보기
