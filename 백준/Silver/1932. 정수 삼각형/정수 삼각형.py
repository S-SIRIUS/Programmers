# 정수삼각형(실버2)
def dp(field, n):
    for i in range(1, n):
        for j in range(0, i+1):

            if j-1>=0:
                field[i][j] = max(field[i-1][j], field[i-1][j-1]) + field[i][j]
            else:
                field[i][j] = field[i-1][j] + field[i][j]
    return field
n = int(input())
field=[[0]*n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(0, len(temp)):
        field[i][t] = temp[t]
field = dp(field,n)
print(max(field[n-1]))