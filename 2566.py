max,row,col=0,0,0
for i in range(9):
    emptylist=list(map(int,input().split()))
    for j in range(9):
        if emptylist[j]>=max:
            max=emptylist[j]
            row=i+1
            col=j+1
print(max)
print(row,col)