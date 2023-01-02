# def isPrime(n):
#     if n==1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True


# while True:
#     n=int(input())
#     primelist=[]
#     if n==0:
#         break
#     else:
#         for i in range(n,2*n+1):
#             if isPrime(i):
#                 primelist.append(i)
#     print(len(primelist))

max=123456*2
primes = [False,False] + [True]*(max-1)

for i in range(2,max+1):
    if primes[i]:
        for j in range(2*i,max+1,i):
            primes[j]=False

while True:
    n=int(input())
    count=0
    if n==0:
        break
    else:
        for i in range(n+1,2*n+1):
            if primes[i]==True:
                count+=1
    print(count)