# 1,2,3 더하기 3 (실버2)
T = int(input())
a = [0]* 1000001
a[1] = 1
a[2] = 2
a[3] = 4

for i in range(4, 1000001):
    a[i] = (a[i-1] + a[i-2] + a[i-3])%1000000009

for i in range(T):
    n = int(input())
    print(a[n])