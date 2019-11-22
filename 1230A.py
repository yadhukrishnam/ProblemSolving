a,b,c,d = list(map(int, input().split()))
print ("YES" if a+b+c == d or a+b+d==c or b+d+c == a or c+a+d == b or a+b == c+d or a+c == b+d or d+a == b+c else "NO" )