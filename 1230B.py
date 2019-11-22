k,n = map(int, input().split())
s = list(input())
i = 0
if n == 0:
    print (''.join(s))
elif len(s) > 1:
    if s[0] == '1':
        n+=1

    s[0] = '1'
    while n!=0 and i<=len(s)-1:
        if s[i] == '0':
            n+=1
        if i!=0:
            s[i] = '0'
        
        i+=1

        n-=1
    print (''.join(s))
else:
    print (0)