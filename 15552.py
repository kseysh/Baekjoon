import sys
num=int(input())
for a in range(num):
	a,b=map(int,sys.stdin.readline().split())
	print(a+b)
