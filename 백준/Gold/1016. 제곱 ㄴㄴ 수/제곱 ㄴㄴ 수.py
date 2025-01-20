# 제곱이 아닌 수 찾기(골드1)
import math
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
check=[True] *(b-a+1)

count=0
for i in range(2, int(math.sqrt(b))+1):
    pow = i*i
    start = math.ceil(a/pow)
    for j in range(start, int(b/pow)+1):
        check[j*pow-a] = False

for i in check:
    if i:
        count+=1
print(count)