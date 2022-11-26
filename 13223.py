hourlist=list(map(int,input().split(':')))
saltthrowhour=list(map(int,input().split(':')))
outputlist=[0,0,0]

def subtracttime(listnumber):
	maxtime=60
	if listnumber==0:
		maxtime=24
	if (saltthrowhour[listnumber]-hourlist[listnumber])<0:
		outputlist[listnumber]=(maxtime+saltthrowhour[listnumber]-hourlist[listnumber])
		saltthrowhour[listnumber-1]-=1
	elif (saltthrowhour[listnumber]-hourlist[listnumber])==0:
		outputlist[listnumber]=0
	else:
		outputlist[listnumber]=(saltthrowhour[listnumber]-hourlist[listnumber])
	if listnumber!=2 and (saltthrowhour[listnumber+1]-hourlist[listnumber+1]<0):		
		if listnumber==1 and outputlist[listnumber-1]<=0:
			outputlist[listnumber-1]=maxtime-1
			
subtracttime(2)
subtracttime(1)
subtracttime(0)

if outputlist[0]==0 and outputlist[1]==0 and outputlist[2]==0:
	outputlist[0]=24
	outputlist[1]=0
	outputlist[2]=0

output=list(map(str,outputlist))

for a in range(3):
	output[a]=output[a].zfill(2)

print(output[0]+':'+output[1]+':'+output[2])