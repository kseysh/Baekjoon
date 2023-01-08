import sys
from collections import Counter
n=int(input())
numberList=[]
for _ in range(n):
    numberList.append(int(sys.stdin.readline()))
cnt=Counter(sorted(numberList,reverse=True)).most_common()
modeIdx=0
for count in range(1,len(cnt)):
    if cnt[0][1]==cnt[count][1]:
        modeIdx=count-1
    else:
        break

print(round(sum(numberList)/n))
print(sorted(numberList)[((n+1)//2)-1])
print(cnt[modeIdx][0])
print(max(numberList)-min(numberList))


#다른 사람의 풀이
from sys import stdin
input = stdin.readline

from collections import Counter
n = int(input())
L = [int(input()) for i in range(n)]
C = Counter(L)
maxfreq = max(C.values())
common = sorted(x for x in C if C[x] == maxfreq)

print(round(sum(L)/n))
print(sorted(L)[n//2])
print(common[1] if len(common) > 1 else common[0])
print(max(L) - min(L))