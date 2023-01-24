import sys
count,saveNum=0,-1

def merge(A,p,q,r):
    tmp=[]
    i=p
    j=q+1
    while i<q and j<r:
        if A[i]<=A[j]:
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1
    while i<=q:
        tmp.append(A[i])
        i+=1
    while j<=r:
        tmp.append(A[j])
        j+=1
    i=p
    while i<=r:
        A=tmp
        i+=1
        count+=1
        if count==k:
            saveNum=A[i]


def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,p+1,r)
        merge(A,p,q,r)

n,k=map(int,input().split())
A=list(map(int,sys.stdin.readline().split()))
merge_sort(A,0,n)
print(saveNum)

