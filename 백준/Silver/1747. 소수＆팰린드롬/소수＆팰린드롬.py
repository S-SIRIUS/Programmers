# 소수&팰린드롬
import math
import sys
input = sys.stdin.readline
def check(data):
    v1 = list(str(data))
    v2 = v1.copy()
    v2.reverse()
    if v1==v2:
        return True
    else:
        return False
m = 2000000
n = int(input())
prime=[True]*(m)
prime[0]=False
prime[1]=False
for i in range(2, int(math.sqrt(m))+1):
    if prime[i]==False:
        continue
    for j in range(2*i, m, i):
        prime[j] = False

for i in range(n, m):
    if prime[i]==True:
        if check(i):
            print(i)
            break