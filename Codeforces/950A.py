
left, right, ambi = map(int, input().split())

while (ambi>0):
    if left < right:
        left+=1
    elif left > right:
        right+=1
    elif left==right and ambi%2==0:
        left+=1
        right+=1
        ambi-=1
    ambi-=1

print (min(left, right)*2)
