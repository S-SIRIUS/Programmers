# 플로이드(골드4)
import sys
input = sys.stdin.readline
inf = int(1e9)
n = int(input())
m = int(input())
matrix = [[inf]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, v = map(int, input().split())
    matrix[a][b] = min(matrix[a][b], v)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            matrix[i][j]=0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j]==inf:
            print(0, end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()