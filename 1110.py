n=int(input())
newint=100
count=0
temp1=n
while n!=newint:
	temp=temp1//10+temp1%10
	newint=10*(temp1%10)+temp%10
	temp1=newint
	count+=1
print(count)