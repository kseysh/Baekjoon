import sys
from bisect import bisect, bisect_left
n=int(input())
sangeunCard=sorted(list(map(int,sys.stdin.readline().split())))
m=int(input())
numberCard=list(map(int,sys.stdin.readline().split()))

for i in numberCard:
    print(bisect(sangeunCard,i)-bisect_left(sangeunCard,i), end=' ')
    
