b = int(input())
g = int(input())
n = int(input())
count = 0
for i in range(n+1):
    if n-i <= g and i<= b:
        count+=1
print (count)