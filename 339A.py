string = input()
ls=[]
for el in string:
    if el !='+':
        ls.append(el)
ls.sort()
for i in range(len(ls)):
    if i!=len(ls)-1:
        print (ls[i], end='+')
    else:
        print (ls[i])
