a,b=map(int,input().split())
memberList=list(map(int,input().split()))
print(sorted(memberList,reverse=True)[b-1])