yc,bc = map(int,input().split())
y, g, b = map(int, input().split())
y = (2*y) + g - yc
x = (3*b) + g - bc
x = (0 if x<0 else x)
y = (0 if y<0 else y)
print (x+y if x+y>=0 else 0)
