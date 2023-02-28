import sys
from collections import deque
queue = deque()
result = deque()
for i in range(int(sys.stdin.readline().rstrip())):
    inputNumber = int(sys.stdin.readline().rstrip())
    if inputNumber == 0:
        if len(queue) == 0:
            result.append(0)
        else:
            minIndex = queue.index(min(queue))
            result.append(queue[minIndex])
            del queue[minIndex]
    else:
        queue.append(inputNumber)
for i in result:
    print(i)