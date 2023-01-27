import sys
n,m=map(int,input().split())
noListenPeople=set()
for i in range(n):
    noListenPeople.add(sys.stdin.readline().rstrip())
noSeePeople=list()
for i in range(m):
    noSeePeople.append(sys.stdin.readline().rstrip())
count=0
tmplist=[]
for people in noSeePeople:
    if people in noListenPeople:
        count+=1
        tmplist.append(people)
print(count)
tmplist.sort()
for i in tmplist:
    print(i)

#다른 사람의 코드

n,m = map(int,input().split())
unheard = set(input() for i in range(n))
unseen = set(input() for i in range(m))
anon = unheard&unseen
print(len(anon))
for i in sorted(anon):
    print(i)