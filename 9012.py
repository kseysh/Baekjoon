def isCorrectVPS(data):
    stack = []
    for j in data:
        if j=='(':
            stack.append(j)
        elif j==')' and len(stack)>0:
            stack.pop()
        else:
            return False
    if len(stack)==0:
        return True
    else:    
        return False

inputNumber = int(input())
for i in range(inputNumber):
    inputData = input()
    if(isCorrectVPS(inputData)):
        print("YES")
    else:
        print("NO")