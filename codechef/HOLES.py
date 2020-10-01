for _ in range(int(input())):
    x = input()
    H1 = 'ADOPQR'
    H2 = 'B'
    count = 0
    for i in range(len(x)):
        if x[i] in H1:
            count+=1
        elif x[i] in H2:
            count+=2
    print (count)

