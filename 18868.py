import sys
m,n=map(int,sys.stdin.readline().split())
universe = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for arr in universe:
    tmpList=sorted(list(set(arr)))
    tmpDic={tmpList[i]:i for i in range(len(tmpList))}
    for j in range(len(arr)):
        arr[j]=tmpDic[arr[j]]
# 문자열, 숫자, 튜플만 set에 넣어 중복 제거 가능

count=0
for i in range(m-1):
    for j in range(i+1,len(universe)):
            if universe[i]==universe[j]:
                count+=1
print(count)
            
