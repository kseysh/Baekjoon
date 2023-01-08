import sys
sortArray=[0]*10001
for i in range(int(input())):
    sortArray[int(sys.stdin.readline())]+=1
for i in range(10001):
    if sortArray[i]!=0:
        for j in range(sortArray[i]):
            print(i)


