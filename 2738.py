n,m=map(int,input().split())
alist=[[0 for j in range(m)]for i in range(n)]#alist[n][m]
for a in range(2):
    for i in range(n):
        emptylist=list(map(int,input().split()))
        for j in range(m):
            alist[i][j]+=emptylist[j]

for i in range(n):
    for j in range(m):
        print(alist[i][j], end=' ')
    print()