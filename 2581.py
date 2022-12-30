def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
m=int(input())
n=int(input())
sumlist=list()
for i in range(m,n+1): #for i in range(int(input()),int(input())+1): 가능
    if isPrime(i):
        sumlist.append(i)
if len(sumlist)!=0: 
    print(sum(sumlist))
    print(min(sumlist))
else:
    print(-1)
