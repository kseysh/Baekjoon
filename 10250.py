num=int(input())
for i in range(num):
	h,w,n=map(int,input().split())
	if n%h!=0:
		floor=n//h+1
		count=n%h
	else:
		floor=n//h
		count=h
	print(str(count)+str(floor).zfill(2))

