input()
string = input().lower()
flag = 0
for el in 'abcdefghijklmnopqrstuvwxyz':
    if el not in string:
        flag = 1
        break

print ("NO" if flag==1 else "YES")
