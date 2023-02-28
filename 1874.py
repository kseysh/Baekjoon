from collections import deque
import sys
maxInteger = int(input())
permutation = deque(range(1,maxInteger+1))
stack = list()
target = deque()
result = list()
plusMinusOutput = list()
for i in range(maxInteger):        
    target.append(int(sys.stdin.readline().rstrip()))
while len(result) != maxInteger:
    if len(stack) == 0:
        stack.append(permutation.popleft())
        plusMinusOutput.append('+')
    elif target[0] == stack[len(stack)-1]:
        result.append(stack.pop())
        target.popleft()
        plusMinusOutput.append('-')
    elif target[0] > stack[len(stack)-1]:
        stack.append(permutation.popleft())
        plusMinusOutput.append('+')
    else :
        plusMinusOutput = list()
        break
if len(plusMinusOutput) == 0:
    print("NO")
else:
    for i in plusMinusOutput:
        print(i)


#다른 사람의 풀이
# list[-1]으로 마지막 인덱스의 값을 가져올 수 있다
# permutation이 아닌 nextnum을 사용하여 쓸데없이 리스트를 사용하는 것을 방지하였다.
# for 문으로 target 리스트를 대체하였고 굳이 result를 이용하지 않았다.

n = int(input())
stack = []
ans = []
nextnum = 1

for i in range(n):
    target = int(input())
    while nextnum <= target:
        stack.append(nextnum)
        ans.append("+")
        nextnum+= 1
    if stack[-1] == target:
        stack.pop()
        ans.append('-')
if stack:
    print("NO")
else:
    for i in ans:
        print(i)