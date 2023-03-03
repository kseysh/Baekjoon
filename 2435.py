day,continuousday = map(int,input().split())
temperatureList = list(map(int,input().split()))
sumMax = -100_000
for i in range(day-continuousday+1):
    compareSum = 0
    for j in range(i,i+continuousday):
        compareSum+=temperatureList[j]
    if compareSum > sumMax:
        sumMax = compareSum
print(sumMax)

#다른 사람의 풀이

n,k = map(int,input().split())
t = list(map(int,input().split()))

s = sum(t[:k])
best = s
for i in range(k,n):
    s+= t[i]-t[i-k]
    best = max(best, s)
print(best)