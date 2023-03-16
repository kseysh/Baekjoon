from collections import deque
commandCount =int(input())
inputCommand = input()
alphabetDeque = deque()
operatorDeque = deque()
alphabetToTargetList = list()
for i in range(commandCount):
    alphabetToTargetList.append(int(input()))

for i in inputCommand:
    if i>='A'and i<='Z':
        alphabetDeque.append(alphabetToTargetList[ord(i)-65])
    else:
        a = alphabetDeque.pop()
        b= alphabetDeque.pop()
        if i=='*':
            alphabetDeque.append(b*a)
        elif i=='/':
            alphabetDeque.append(b/a)
        elif i=='+':
            alphabetDeque.append(b+a)
        elif i=='-':
            alphabetDeque.append(b-a)


print(format(alphabetDeque.pop(),".2f"))