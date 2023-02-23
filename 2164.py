number = int(input())
card = list(range(number,0,-2))

while len(card)!=1:
    card.pop()
    card.insert(0,card.pop())
print(card[0])
# 시간 초과

input = int(input())
square = 2

while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break

# 다른 사람의 풀이

from collections import deque

d = deque()
n = int(input())
for i in range(1,n+1):
    d.append(i)
for i in range(1,n+1):
    if len(d) == 1:
        print(d.pop())
        break
    d.popleft()
    new = d.popleft()
    d.append(new)