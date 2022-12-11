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
print(arr)

#다른 사람의 풀이
n = int(input())
c = 0
while n%5 != 0:
    n-= 3
    c+= 1
if n < 0:
    print(-1)
else:
    print(c+n//5)