# 실버4 네모네모 시력검사
# 1) 정사각형의 변의 길이를 찾는다. #이 있는 4가지 방향으로 가본다음 가장 긴 길이가 변의 길이 
# 2) 찾은 맨왼쪽 위 지점부터 UP:(x+n//2) -> RIGHT(y-n//2) -> DOWN:(x-n//2) -> LEFT:(y+n//2)를 해서 점을 확인한다.

def find_n(x,y):
    up_count=0
    down_count=0
    left_count=0
    right_count=0

    if grid[x+1][y] == "#":
        for i in range(1, n-x):
            if grid[x+i][y]==".":
                break
            else:
                up_count+=1

    if grid[x-1][y] == "#" :
        for i in range(1, x):
            if grid[x-i][y]==".":
                break
            else:
                down_count+=1
    
    if grid[x][y-1] == "#":
        for i in range(1, y):
            if grid[x][y-i]==".":
                break
            else:
                left_count+=1
    
    if grid[x][y+1] == "#":
        for i in range(1, m-y):
            if grid[x][y+i]==".":
                break
            else:
                right_count+=1
    return max(up_count, down_count, left_count, right_count)

def find_location(x, y, n):
    if grid[x][y+n//2] == '.':
        return "UP"
    elif grid[x+n//2][y+n-1]=='.':
        return "RIGHT"
    elif grid[x+n-1][y+n-1-(n//2)]=='.':
        return "DOWN"
    else:
        return "LEFT"


n, m = map(int, input().split())
grid=[]
for i in range(n):
    grid.append(list(input()))


for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            square_n = find_n(i,j)+1
            print(find_location(i, j, square_n))
            exit(0)