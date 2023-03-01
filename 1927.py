from heapq import heappop, heappush
import sys
min_heap = []
result = []

for i in range(int(input())):
    inputNumber = int(sys.stdin.readline().rstrip())
    if inputNumber == 0:
        if len(min_heap) == 0:
            result.append(0)
        else:
            result.append(heappop(min_heap))
    else:
        heappush(min_heap,inputNumber)
for i in result:
    print(i)