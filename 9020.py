max=10000
prime_list=[False,False]+[True]*(max-1)
for j in range(2,max+1):
    if prime_list[j]:
        for k in range(2*j,max+1,j):
            prime_list[k]=False

for i in range(int(input())):
    num=int(input())
    for j in range(num//2,1,-1):
        if prime_list[j] and prime_list[num-j]:
            print(str(j)+' '+str(num-j))
            break
        

#int()를 이용하여 float를 정수로 변환하면 소수 부분을 제외한 정수를 리턴