for _ in range(int(input())):
    x,y = input().split()
    y = int(y)
    z = list(map(int, input().split()))
    op = ""
    for i in range(len(z)):
        if (y >= z[i]):
            y-=z[i]
            op+='1'
        else:
            op+='0'
    print (op)


