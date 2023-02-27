from collections import deque
n,k = map(int,input().split())
queue = deque(range(1,n+1))
result = []
while len(queue)!=0:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print(str(result).replace('[','<').replace(']','>'))    

