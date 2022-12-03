import math
a,b=map(int,input().split())

def checknumber(n):
	if n==1:
		return False
	for j in range(2,int(math.sqrt(n))+1):
		if i%j==0:
			return False
	return True

for i in range(a,b+1):
	if checknumber(i):
		print(i)

# sqrt 대신 num**0.5도 가능

m,n = map(int,input().split())
prime = [1]*(n+1)
prime[0] = 0
prime[1] = 1
for i in range(2,n+1):
    if i>=m and prime[i]:
        print(i)
    if prime[i]:
        for j in range(2*i,n+1,i):
            prime[j] = 0
