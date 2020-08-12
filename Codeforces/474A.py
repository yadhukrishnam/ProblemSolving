def shift(string, dir='L'):
    key1,key2,key3 = "qwertyuiop", "asdfghjkl;", "zxcvbnm,./"
    newStr = ""

    shift = (-1 if dir=='L' else 1)
    ls =[ ( key1.index(ch) if ch in key1 else (   ))  for ch in string] 
    print (ls) 
    for ch in string:
        
        if ch in key1:
            ls.append(key1.index(ch))
        elif ch in key2:
            ls.append(key2.index(ch))
        elif ch in key3:
            ls.append(key3.index(ch))

    shift *= (min(ls) if shift!='L' else max(ls) )

    for ch in string:
        if ch in key1:
            newStr += (key1[key1.index(ch) + shift])
        elif ch in key2:
            newStr += (key2[key2.index(ch) + shift])
        elif ch in key3:
            newStr += (key3[key3.index(ch) + shift])
    return newStr
print (shift("s;;upimrrfod;pbr"))