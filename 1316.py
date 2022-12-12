count=0
for i in range(int(input())):
    alphabet=input()
    error=0
    for j in range(len(alphabet)-1):
        if alphabet[j]!=alphabet[j+1]:
            for k in range(1,len(alphabet)-j):
                if alphabet[j]==alphabet[j+k]:
                    error+=1
    if error==0:
        count+=1
print(count)

#다른 사람의 풀이

def grouped(w):
    for c in "abcdefghijklmnopqrstuvwxyz":
        while c+c in w: w = w.replace(c+c, c)
    return len(set(w)) == len(w)

print(sum(map(grouped, [input() for i in range(int(input()))])))