import sys
num=int(input())
sum=0
data=list(map(int,sys.stdin.readline().rstrip()))
for a in range(num):
	sum+=data[a]
print(sum)