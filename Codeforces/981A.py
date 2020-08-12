s,i = input(),0
while s==s[::-1] and len(s)!=0 : s = s[:i:-1]
print ("0" if len(s)==0 else len(s))

