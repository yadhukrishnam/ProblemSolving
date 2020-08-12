matrix = []
while (len(matrix)!=5):
    matrix.append(list(map(int,input().split())))

flag = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            flag = 1
            break
    if flag==1:
        break
i+=1
j+=1
steps = abs(3-i) + abs(3-j)
print (steps)
