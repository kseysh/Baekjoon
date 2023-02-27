from collections import deque
import sys
for i in range(int(input())):   
    documentCount, targetIndex = map(int,sys.stdin.readline().split())
    printer = deque(map(int,sys.stdin.readline().split()))
    count =1
    while len(printer)!=0:
        currentMaxIndex = printer.index(max(printer))
        if currentMaxIndex == targetIndex:
            print(count)
            break
        for i in range(currentMaxIndex):
            printer.append(printer.popleft())
            if targetIndex == 0:
                targetIndex=len(printer)-1
            else:
                targetIndex -= 1
                currentMaxIndex -=1
        printer.popleft()
        targetIndex -= 1
        currentMaxIndex -=1
        count+=1


