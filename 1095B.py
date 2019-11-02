input()
ls = sorted(list(map(int, input().split())))
print ((ls[len(ls)-2] - ls [0]) if ls[len(ls)-2] - ls [0] < (ls[len(ls)-1] - ls [1]) else (ls[len(ls)-1] - ls [1]))
