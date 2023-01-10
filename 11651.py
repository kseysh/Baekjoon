import sys
nList=[list(map(int,sys.stdin.readline().split())) for _ in range(int(input()))]
nList=sorted(nList,key=lambda x:(x[1],x[0]))
for i in range(len(nList)):
    print(nList[i][0],nList[i][1])