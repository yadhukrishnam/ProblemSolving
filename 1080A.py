from math import ceil as c
n,k = map(int, input().split())
print ((c(2*n/k)+c(5*n/k)+c(8*n/k)))
