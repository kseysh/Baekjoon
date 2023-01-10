import sys
n=int(input())
nList=list(map(int,sys.stdin.readline().split()))
tempList=sorted(list(set(nList)))
tempDic={tempList[i]:i for i in range(len(tempList))}
for i in nList:
    print(tempDic[i],end=' ' )

