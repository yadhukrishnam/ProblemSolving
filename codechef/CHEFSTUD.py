for _ in range(int(input())):
    count = 0
    x = list(str(input()))
    for i in range(len(x)):
        if x[i]== '>':
            x[i]= '<'
        elif x[i] == '<':
            x[i] = '>'
    for i in range(len(x)-1):
        if (x[i] == '>' and x[i+1] == '<'):
            count+=1
    print (count)
