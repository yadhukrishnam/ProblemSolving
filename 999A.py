a,max = map(int, input().split())
ls = list(map(int, input().split()))
count = 0
for el in ls:
    if el <= max:
        count+=1
    else:
        break
ls = ls[count:]
for el in ls[::-1]:
    if el <= max:
        count+=1
    else:
        break
print  (count)
