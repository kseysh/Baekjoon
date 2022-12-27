string = input().upper()
tempdic={}
for a in range(len(string)):
	if string[a] not in tempdic:
		tempdic[string[a]]=1
	else:
		tempdic[string[a]]+=1


count=0
for key,value in tempdic.items():
	if max(tempdic.values())==int(value):
		count+=1

tempdic={v:k for k,v in tempdic.items()}

if count>1:
	print('?')
else:
	print(tempdic.get(max(tempdic)))

#key로 value 출력시 tempdic['a'] 나 tempdic.get('a') 둘 다 가능

#다른 사람의 풀이

from collections import Counter
C = Counter(input().upper())
cv = list(C.values())
if cv.count(max(cv)) > 1: print("?")
else: print(C.most_common(1)[0][0])