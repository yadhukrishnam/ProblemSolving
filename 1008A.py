s = input().lower()
con = list('bcdfghjklmnpqrstvwxyz')
vow = list("aeiou")
flag = 1
for i in range(len(s)):
    if s[i] in con and s[i]!='n':
        if s[i+1] not in vow:
            flag = 0
            break
print ("YES" if flag else "NO")
