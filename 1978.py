arr=[1]*1001
arr[1]=0
for i in range(2,int(1001)):
    for j in range(2,int(1+1001**0.5)):
        if i*j<=1000:
            arr[i*j]=0
num=int(input())
arr1=list(map(int,input().split()))
count=0
for i in range(num):
    if arr[arr1[i]]:
        count+=1
print(count)


#다른 사람의 풀이
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

input()
print(sum(map(prime,map(int,input().split()))))