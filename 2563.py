whitePaper=[[0 for j in range(100)] for i in range(100)]
count=0
for a in range(int(input())):
    x,y=map(int,input().split())
    for i in range(10):
        for j in range(10):
            if whitePaper[x+i][y+j]==0:
                whitePaper[x+i][y+j]=1
                count+=1
print(count)


black = set()
for T in range(int(input())):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            black.add((i,j)) #튜플로 저장
            print(black)
print(len(black))