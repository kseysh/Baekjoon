def trinumber(k,n):
    numberlist=list(range(0,n+1))
    nextnumberlist=list(range(0,n+1))
    for k in range(k): #층수 확인용
        numberlist=nextnumberlist.copy()
        for i in range(1,n+1): #n호까지 돌기
            count=0
            for j in range(1,i+1): #현재 있는 호 사람 수 구해주기
                count+=numberlist[j]
            nextnumberlist[i]=count
    return nextnumberlist[n]


#list_B = list_A.copy()  # 1번 방법
#list_B = list_A[:]		# 2번 방법  

for i in range(int(input())):
    k=int(input())
    n=int(input())
    print(trinumber(k,n))



# 2층 1 4 10
# 1층 1 3 6 10 ...
# 0층 1 2 3 4 5 6 7 ...n