import sys
a,b=map(int,sys.stdin.readline().split())
time=a*60+b
if time-45<0:
	time=time+1440-45
else :
	time-=45
hour=time//60
min=time%60
print(hour,min)
