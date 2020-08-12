math  = input().split('+')
math.sort()
for i in range(len(math)):
    print (math[i], end='')
    if i!=len(math)-1:
        print ('+', end='')

