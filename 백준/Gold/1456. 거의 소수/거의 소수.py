# 거의 소수 구하기(골드5)
import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())

field=[True]*(10000001)
field[0]=False
field[1]=False
for i in range(2, int(math.sqrt(len(field)))+1):
    if field[i]==False:
        continue
    for j in range(i*2, len(field), i):
        field[j]=False
total=0
for i in range(2, len(field)):
    if field[i]==True:
        temp = i
        while i<= b/temp:
            if i >= a/temp:
                total+=1
            temp = temp*i
print(total)