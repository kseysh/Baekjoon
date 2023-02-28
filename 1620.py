import sys
pocketmonCount, problemCount = map(int,input().split())
encyclopedia = dict()
for i in range(1, pocketmonCount+1):
    encyclopedia[sys.stdin.readline().rstrip()] = i
convertEncyclopedia =dict(map(reversed,encyclopedia.items()))
for j in range(problemCount):
    inputString = sys.stdin.readline().rstrip()
    if inputString.isdigit():
        print(convertEncyclopedia.get(int(inputString)))
    else :
        print(encyclopedia[inputString])

# 다른 사람의 풀이
# 한 딕셔너리에 필요한 두가지 값을 넣었다.

import sys; input = sys.stdin.readline
N, M = map(int, input().split())
pokemon = dict()
for i in range(1, N + 1):
    name = input().strip()
    pokemon[i] = name
    pokemon[name] = i
for _ in range(M):
    quiz = input().strip()
    if quiz.isdigit():
        print(pokemon[int(quiz)])
    else:
        print(pokemon[quiz])

