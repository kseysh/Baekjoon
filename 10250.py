num=int(input())
for j in range(num):
	h,w,n=map(int,input().split())
	if n%h!=0:
		count=n%h
	else:
		floor=n//h
		count=h
	print(str(count)+str(floor).zfill(2))

#다른방식으로도 해보기 
