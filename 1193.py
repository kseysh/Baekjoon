#1째 반복 1/1
#2째 반복 내려감 1/2 => 2/1
#3째 반복 올라감 3/1 => 2/2 => 1/3
#4째 반복 내려감 1/4 => 2/3 => 3/2 => 4/1

#1 2 3 4
#1 3 6 10


n = int(input())
 
num = 0
count = 0
 
while num < n:
  num += count
  count +=1

if count%2==1:
	print(str(count-1+n-num)+'/'+str(1+num-n))
else:
	print(str(1+num-n)+'/'+str(count-1+n-num))

#count= 1 recur =1
#count = 3 recur =2
#count =6 recur =3