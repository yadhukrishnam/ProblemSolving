for _ in range(int(input())):
    n,x,b,a = map(int, input().split())
    b,a = max(a,b), min(a,b)
    while ((a!=1 or b!=n) and x!=0):
            if a!=1:
                a-=1
                x-=1
            if b!=n and x!=0:
                b+=1
                x-=1
    print (abs(a-b))
             
