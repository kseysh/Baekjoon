sum = 0
mushroom = list()
count = 0
for i in range(10):
    mushroom.append(int(input()))
for i in range(10):
    if sum>=100:
        break
    sum+=mushroom[count]
    count+=1
beforeSum=sum-mushroom[count-1]
if sum-100 <= 100-beforeSum:
    print(sum)
else:
    print(beforeSum) 

