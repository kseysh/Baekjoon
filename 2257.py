chemical=input()
tempDic={'H':1,'C':12,'O':16}
stack=[]
for i in chemical:
    if i=='(':
        stack.append(i)
    elif i==')':
        tempCount=0
        while True:
            target=stack.pop()
            if target=='(':
                break
            else:
                tempCount+=target
        stack.append(tempCount)
    # elif i=='H':
    #     stack.append(tempDic('H'))
    # elif i=='C':
    #     stack.append(tempDic('C'))
    # elif i=='O':
    #     stack.append(tempDic('O'))
    elif i in tempDic:
        stack.append(tempDic[i])
    else:
        stack[-1]*=int(i)

print(sum(stack))
