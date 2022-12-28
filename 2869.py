import math
a,b,v=map(int,input().split())
print(math.ceil((v-b)/(a-b)))



# day(a-b)+b>v
# day>v-b/(a-b)