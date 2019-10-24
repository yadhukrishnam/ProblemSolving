n=int(input())
x,y=map(int, input().split())
print ("black" if abs(x-n)+abs(y-n) < abs(x-1)+abs(y-1) else "white"  )
