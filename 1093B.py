for _ in range(int(input())):
    x = input()
    a,flag = x[0],True

    for el in x:
        if el != a:
            flag = False

    if flag:
        print (-1)
    elif x == x[::-1]:
        print (x[1:],x[0], sep='')
    else:
        print (x)
