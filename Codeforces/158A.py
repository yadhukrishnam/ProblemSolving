n,k = map(int,input().split())
ls = list(map(int, input().split()))
ls.sort()
ls.reverse()
newList = ls[k:]
k+=newList.count(ls[k-1])
if ls[0]!=0:
    print (k)
else:
    print (0)
