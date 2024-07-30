# RGB거리(실버1)

n = int(input())
RGB = []
for i in range(n):
    RGB.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, 3):
        if j==0:
            RGB[i][j] += min(RGB[i-1][1], RGB[i-1][2])
        elif j == 1:
             RGB[i][j] += min(RGB[i-1][0], RGB[i-1][2])
        else:
             RGB[i][j] += min(RGB[i-1][0], RGB[i-1][1])
print(min(RGB[n-1]))