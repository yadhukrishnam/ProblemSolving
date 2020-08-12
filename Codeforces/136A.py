n = int(input())
ls = list(map(int, input().split()))
[ print (ls.index(i)+1, end=" ") for i in range(1, n+1) ]

