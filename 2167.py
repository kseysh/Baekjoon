import sys
n,m = map(int,sys.stdin.readline().split())
numberList = []
resultList = []
coordinateList = []
for i in range(n):
    numberList.append(list(map(int,sys.stdin.readline().split())))
for i in range(int(input())):
    coordinateList = list(map(int,sys.stdin.readline().split()))
    sum = 0
    for j in range(coordinateList[0]-1,coordinateList[2]):
        for k in range(coordinateList[1]-1,coordinateList[3]):
            sum += numberList[j][k]
    resultList.append(sum)
for i in resultList:
    print(i)