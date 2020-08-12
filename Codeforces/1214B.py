b = int(input())
g = int(input())
n = int(input())
count = 0
for i in range(n-g, n):
    for j in range(g, i-g):
        print (i,j)
        count+=1
print (count)