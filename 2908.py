a,b=map(list,input().split())
a[0],a[2]=a[2],a[0]
b[0],b[2]=b[2],b[0]
aa=''
bb=''
for i in range(3):
    aa+=a[i]
    bb+=b[i]
print(aa if int(aa)>int(bb) else bb)

#다른 사람의 풀이
rev = lambda n: int(str(n)[::-1])
x,y = map(int, input().split())
print(max(rev(x),rev(y)))