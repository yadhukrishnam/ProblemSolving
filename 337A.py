n,m = map(int, input().split())
ls = list(map(int, input().split()))
diff = []
for i in range(len(ls)):
    if i+n < len (ls):
        diff.append(abs(ls[i]-ls[i+n]))
    else:
        break
print (diff)

