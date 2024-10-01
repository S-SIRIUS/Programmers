# 미세먼지 안녕!(골드4)
import sys
import copy
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0 , 0, 1, -1]

def ext(extend_target):
    temp_field = copy.deepcopy(field)
    
    for x,y in extend_target:
        division = field[x][y] // 5

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if (0<=new_x<r and 0<=new_y<c and field[new_x][new_y]!=-1):
                temp_field[new_x][new_y] += division
                temp_field[x][y] -= division   
    return temp_field

def air(original, x):
    change = copy.deepcopy(original)
    change[x][1]=0
    for i in range(1, c-1):
        change[x][i+1] = original[x][i]   
    for i in range(0, x):
        change[i][c-1] = original[i+1][c-1]  
    for i in range(0, c-1):
        change[0][i] = original[0][i+1]
    for i in range(1, x):
        change[i][0] = original[i-1][0]
    return change

def air2(original, x):
    change = copy.deepcopy(original)
    change[x][1]=0
    for i in range(1, c-1):
        change[x][i+1] = original[x][i]   
    for i in range(x+1, r):
        change[i][c-1] = original[i-1][c-1]  
    for i in range(0, c-1):
        change[r-1][i] = original[r-1][i+1]
    for i in range(x+1, r-1):
        change[i][0] = original[i+1][0]
    return change

r, c, t = map(int, input().split())
field=[]
for i in range(r):
    field.append(list(map(int, input().split())))

for k in range(t):
    extend_target=[]
    for i in range(r):
        for j in range(c):
            if field[i][j]!=0 and field[i][j]!=-1:
                extend_target.append((i,j))
    field = ext(extend_target)
    
    for i in range(r):
        if field[i][0]==-1:
            field = air(field, i)
            field = air2(field, i+1)
            break

answer=0
for i in field:
    answer += sum(i)
print(answer+2)
