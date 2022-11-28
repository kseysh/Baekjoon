import sys
casecount=int(input())
for a in range(casecount):
	temparr=list(map(int,sys.stdin.readline().split()))
	sum=0
	for b in range(1,temparr[0]+1):
		sum+=temparr[b]
	averageval=sum/temparr[0]
	count=0
	for c in range(1,temparr[0]+1):
		if temparr[c]>averageval:
			count+=1
	print('%.3f%%'%(count/temparr[0]*100))
