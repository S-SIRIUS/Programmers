# 이동하기(실버2)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field=[[0]*(m+1)]
for i in range(n):
    field.append([0]+list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        field[i][j] += max(field[i-1][j], field[i][j-1], field[i-1][j-1])

print(field[n][m])