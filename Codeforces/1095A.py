len = int(input())
s = input()
n = 0
while (n*(n+1)//2)<len-1:
    print (s[n*(n+1)//2], end='')
    n+=1
print(s[0] if n==0 else "")
