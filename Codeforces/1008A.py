s = input().lower()
con = list('bcdfghjklmnpqrstvwxyz')
vow = list("aeiou")
flag = 1
if len(s)==1 and s in con and s!='n':
    print ("NO")
elif s[len(s)-1] in con and s[len(s)-1]!='n':
    print ("NO")
else:
    for i in range(len(s)):
        if s[i] in con and s[i]!='n':
                if s[i+1] not in vow:
                    flag = 0
                    break
    print ("YES" if flag else "NO")
