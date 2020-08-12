strA = input()
strB = input()
endA = len(strA)-1
endB = len(strB)-1
while (strA[endA] == strB[endB] and endA>=0 and endB>=0):
    endA -=1
    endB -=1
print (endA+endB+2)
