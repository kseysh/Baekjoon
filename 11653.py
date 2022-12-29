num=int(input())
count=2
while num!=1:
    while True:
        if num%count!=0:
            break
        else:
            num/=count
            print(count)
    count+=1