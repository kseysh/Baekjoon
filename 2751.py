sortArray=[0]*1000001
for i in range(int(input())):
    sortArray[int(input())]+=1
for i in range(1000001):
    if sortArray[i]:
        print(i) 
#시간복잡도 O(N+K) 계수 정렬 실패

sortArray=[]
for i in range(int(input())):
    sortArray.append(int(input()))
for i in sorted(sortArray):
    print(i)
# sorted()를 이용한 시간 복잡도 O(nlogn) Timsort 알고리즘 실패

import sys
sortArray=[]
for i in range(int(input())):
    sortArray.append(int(sys.stdin.readline()))
for i in sorted(sortArray):
    print(i)
#stdin.readline()을 사용하여 성공 값을 많이 input할시 사용할 것


         




