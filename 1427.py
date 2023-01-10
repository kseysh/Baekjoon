n=input()
nList=[]
for i in range(len(n)):
    nList.append(n[i])

nList.sort(reverse=True)
for j in range(len(nList)):
    print(nList[j],end='')

#다른 사람의 풀이
print(''.join(sorted(input()))[::-1])