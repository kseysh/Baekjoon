# import sys
# nList=[list(map(int,sys.stdin.readline().split())) for _ in range(int(input()))]
# for i in range(len(nList)):
#     print(sorted(nList,key=lambda x:(x[1],x[0]))[i])

# import sys
# num=int(input())
# strList=list()
# for i in range(num):
#     strList.append(sys.stdin.readline().strip())

# strList=sorted(list(set(strList)))
# strList.sort(key=len)

# for i in range(len(strList)):
#     print(strList[i])

#다른 사람의 풀이
for s in sorted(set([input() for n in range(int(input()))]), key=lambda x:(len(x),x)):
    print(s)
# sort함수에서의 key값은 여러개의 요소를 기준으로 정렬할 경우 튜플을 사용 할 수도 있다.
