k,n,w = map(int, input().split())
x = (k*w*(w+1)//2)-n
print (x if x > 0 else 0)
