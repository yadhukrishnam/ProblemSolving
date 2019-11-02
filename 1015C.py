n,m = map(int, input().split())
diffLs = []
currentUsage = 0
for i in range (n):
    a,b = map(int, input().split())
    diffLs.append(abs(a-b))
    currentUsage+=a

diffLs.sort()
diffLs = diffLs[::-1]
count = 0
while currentUsage > m:
    if len(diffLs) == 0:
        count = -1
        break
    else:
        count+=1
        currentUsage-=diffLs.pop(0)

print (count)



