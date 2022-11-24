def recursion(s, l, r):
    global count
    count+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count=0
    return recursion(s, 0, len(s)-1)

num=int(input())

arr=[]
for a in range(num):
    arr.append(input())

for a in range(num):
    print(isPalindrome(arr[a]),count,end=' ')
    print()

