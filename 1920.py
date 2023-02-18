inputFirstNumber = int(input())
firstList = set(map(int, input().split()))
inputSecondNumber = int(input())
secondList = list(map(int, input().split()))

for target in secondList:
    print(1) if target in firstList else print(0)