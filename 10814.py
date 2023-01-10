import sys
memberList=[]
for i in range(int(input())):
    memberList.append(list(map(str,sys.stdin.readline().split())))
memberList.sort(key=lambda x: int(x[0]))
for j in range(len(memberList)):
    print(memberList[j][0],memberList[j][1])
    