import sys
stack = []
for i in range(int(input())):
    inputList = list(sys.stdin.readline().split())
    if inputList[0] == 'push':
        stack.append(inputList[1])
    elif inputList[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif inputList[0] == 'size':
        print(len(stack))
    elif inputList[0] == 'empty':
        if len(stack)==0:
            print(1)
        else :
            print(0)
    elif inputList[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])


#다른 사람의 풀이
#띄어쓰기까지 한 번에 받아 구분하였다
from sys import stdin
input = stdin.readline
stack = []
n = int(input())
for i in range(n):
    s = input().rstrip()
    if s[:4] == "push":
        stack.append(int(s[5:]))
    elif s == "pop":
        print(stack.pop() if stack else -1)
    elif s == "size":
        print(len(stack))
    elif s == "empty":
        print(0 if stack else 1)
    elif s == "top":
        print(stack[-1] if stack else -1)