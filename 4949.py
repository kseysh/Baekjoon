import sys
while True:
    stack = []
    inputString = sys.stdin.readline().rstrip()
    if inputString == '.':
        break
    for i in inputString:
        if i == '[':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ']' :
            if len(stack)>=1 and stack[len(stack)-1] == '[':
                stack.pop()
            else:
                stack.append("false")
                break
        elif i == ')' :
            if len(stack)>=1 and stack[len(stack)-1] == '(' :
                stack.pop()
            else:
                stack.append("false")
                break
    if len(stack) != 0 :
        print("no")
    else:
        print("yes")
