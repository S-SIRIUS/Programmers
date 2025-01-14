# 소수 구하기
import sys
import math
input = sys.stdin.readline
m, n = map(int, input().split())
field=[True]*(n+1)
field[0]=False
field[1]=False

for i in range(2, int(math.sqrt(n))+1):
    if field[i]==False:
            continue
    for j in range(2*i, n+1, i):
        field[j] = False

for i in range(m, n+1):
    if field[i]==True:
        print(i)