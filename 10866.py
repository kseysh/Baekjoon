from collections import deque
import sys
saveInt = deque()
for i in range(int(input())):
    command = sys.stdin.readline().rstrip()

    if command[:10] == 'push_front':
        saveInt.appendleft(command[11:])
    elif command[:9] == 'push_back':
        saveInt.append(command[10:])
    elif command == 'pop_front':
        if len(saveInt)==0:
            print(-1)
        else:
            print(saveInt.popleft())
    elif command == 'pop_back':
        if len(saveInt)==0:
            print(-1)
        else:
            print(saveInt.pop())
    elif command == 'size':
        print(len(saveInt))
    elif command == 'empty':
        if len(saveInt) == 0:
            print(1)
        else :
            print(0)
    elif command == 'front':
        if len(saveInt) == 0:
            print(-1)
        else :
            print(saveInt[0])
    elif command == 'back':
        if len(saveInt) == 0:
            print(-1)
        else :
            print(saveInt[len(saveInt)-1])
