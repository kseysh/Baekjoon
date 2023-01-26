import sys
n=int(input())
sangeunCard=sorted(list(map(int,sys.stdin.readline().split())))
m=int(input())
numberCard=list(map(int,sys.stdin.readline().split()))

def binarySearch(cardList,target):
    lower=0
    upper=len(cardList)-1
    while lower<=upper:
        mid=(lower+upper)//2
        if cardList[mid]==target:
            return 1
        elif cardList[mid]>target:
            upper=mid-1
        else:
            lower=mid+1

    return 0

for i in numberCard:
    print(binarySearch(sangeunCard,i),end=' ')
# bisect함수를 이용해 binarySearch를 쉽게 구현할 수 있다.

n = int(input())
card = set(map(int,input().split()))
m = int(input())
for x in map(int,input().split()):
    print(1 if x in card else 0, end=' ')
#set을 활용하면 무조건 O(1) 즉 상수 시간으로 특정 원소의 유무검사를 해준다.
    
