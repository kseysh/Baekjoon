a=list(map(int,input().split()))
chess=[1,1,2,2,2,8]
def aa(i,num):
    if a[i]==num:
        a[i]=0         
    else:
        a[i]=num-a[i]

for j in range(6):
    aa(j,chess[j])
    print(a[j], end=' ')
