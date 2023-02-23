import sys
beforeMoney = []
account = 0
for i in range(int(input())):
    money = int(sys.stdin.readline().rstrip())
    if money == 0:
        account-=beforeMoney.pop()
        
    else:
        beforeMoney.append(money)
        account += money
print(account)

#다른 사람의 풀이

s=[]
for i in range(int(input())):
    n = int(input())
    if n == 0:
        s.pop()
    else:
        s.append(n)
print(sum(s))