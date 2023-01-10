n=int(input())
nList=[[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    nList[i][0],nList[i][1]=map(int,input().split())
nList.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(nList[i][0],nList[i][1])

#다른 사람의 풀이
for p in sorted([tuple(map(int,input().split())) for i in range(int(input()))]):
    print(p[0], p[1])