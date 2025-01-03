import sys
n, m = map(int, sys.stdin.readline().split())
data = [0]+list(map(int, sys.stdin.readline().split()))
for i in range(1, n+1):
    data[i] = data[i] + data[i-1]
for i in range(0, m):
    start, end = map(int, sys.stdin.readline().split())
    ans = data[end] - data[start-1]
    sys.stdout.write(str(ans)+'\n')