a,b,c=map(int,input().split())
count=0
if b>=c:
	count=-1
else:
	count=a//(c-b)+1
print(count)
