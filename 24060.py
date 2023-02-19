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

// 다른 풀이
count,result=0,-1
def mergeSort(A,start,end):
    if start<end:
        mid=(start+end)//2
        mergeSort(A,start,mid)
        mergeSort(A,mid+1,end)
        merge(A,start,mid,end)

def merge(A,start,mid,end):
    global count,result
    tmp=[]
    s=start
    m=mid+1
    e=end
    t=0
    while s<=mid and m <= end:
        if A[s]>=A[m]:
            tmp.append(A[m])
            m+=1
        else:
            tmp.append(A[s])
            s+=1
        t+=1
    while s<=mid:
        tmp.append(A[s])
        s+=1
        t+=1
    while m<=end:
        tmp.append(A[m])
        m+=1
        t+=1
    s=start
    t=0
    while s<=end:
        count+=1
        A[s]=tmp[t]
        if count==k:
            result=tmp[t]
        s+=1
        t+=1

n,k=map(int,input().split())
aList=list(map(int,sys.stdin.readline().split()))
mergeSort(aList,0,n-1)
print(result)
