num,num1=map(int,input().split())
divisorlist=list()
for i in range(1,num+1):
    if num%i==0:
        divisorlist.append(i)
if len(divisorlist)>num1-1:
    print(divisorlist[num1-1])
else :
    print(0)
