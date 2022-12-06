#런타임 에러가 났던 나의 풀이
arr=[1]*(10001)
def checkselfnumber(n):
	n=n+sum(map(int,str(n)))
	arr[n]=0

for a in range(1,10001):
	checkselfnumber(a)
	if arr[a]:
		print(a)


# 블로그 보고 참고한 풀이
def checkselfnumber(n):
	n=n+sum(map(int,str(n)))
	return n

noSelfNumber=set()

for i in range(1,10001):
	noSelfNumber.add(checkselfnumber(i))

for i in range(1, 10001):
	if i not in noSelfNumber:
		print(i)


#멘토의 풀이
def d(n):
    return n+sum(map(int,list(str(n))))

self = [True]*10001
for i in range(10001):
    q = d(i)
    if q < 10001:
        self[q] = False
for i in range(10001):
    if self[i]:
        print(i)