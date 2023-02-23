import sys
count = int(input())
targetSet = set()
for i in range(count):
    inputList = []
    inputList = list(sys.stdin.readline().split())
    if inputList[0] == 'add':
        targetSet.add(inputList[1])
    elif inputList[0] == 'remove':
        if inputList[1] in targetSet:
                targetSet.remove(inputList[1])
    elif inputList[0] == 'check':
        if inputList[1] in targetSet:
            print(1)
        else:
            print(0)
    elif inputList[0] == 'toggle':
        if inputList[1] in targetSet:
            targetSet.remove(inputList[1])
        else:
            targetSet.add(inputList[1])
    elif inputList[0] == 'all':
        targetSet = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif inputList[0] == 'empty':
        targetSet = set()