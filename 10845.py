import sys
queue = []
for i in range(int(input())):
    inputValue = sys.stdin.readline().rstrip()
    if inputValue[:4] == 'push':
        queue.append(inputValue[5:])
    elif inputValue == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif inputValue == 'size':
        print(len(queue))
    elif inputValue == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif inputValue == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif inputValue == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

# 스택과 큐의 차이점 제대로 알기!