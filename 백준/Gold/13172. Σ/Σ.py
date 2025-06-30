import sys
input = sys.stdin.readline

mod = 1000000007

m = int(input())

def cal(num,x):
  if x == 1:
    return num
  v = cal(n,x//2)
  if x%2 == 0:
    return v*v%mod
  else:
    return v*v*num%mod

count = 0
for i in range(m):
  n,s = map(int,input().split())
  rN = cal(n,mod-2)
  count = (count + rN*s%mod)%mod
print(count)