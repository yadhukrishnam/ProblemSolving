n,m = map(int, input().split())
sum = n
while n!=0:
    sum = sum + n%m
    n = n//m