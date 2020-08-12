x,y = map(int, input().split())
k, m = map(int, input().split())
print("YES" if (list(map(int, input().split()))[k-1]<list(map(int, input().split()))[y-m]) else "NO" )