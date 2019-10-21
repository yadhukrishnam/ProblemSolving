import string
alpha = string.ascii_lowercase
line = str(input()).lower()
score = 0
for ch in alpha:
    if ch in line:
        score+=1
if score%2==0:
    print ("CHAT WITH HER!")
else:
    print ("IGNORE HIM!")
