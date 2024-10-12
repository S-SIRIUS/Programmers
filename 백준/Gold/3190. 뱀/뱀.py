# 뱀(골드4)
from collections import deque

dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]

def way_check(way_str, current_way):
    if way_str=="L":
        current_way+=1
        if current_way>3:
            current_way=0
        return current_way

    elif way_str=="D":
        current_way-=1
        if current_way<0:
            current_way = 3
        return current_way
 

def snake_move(current_way):
    queue = deque()
    second=0
    x = 0
    y = 0
    field[x][y]=-1
    queue.append((x,y))
    while True:
        second+=1
         
        x = x + dx[current_way]
        y = y + dy[current_way]

        if len(way_change)!=0 and second == way_change[0][0]:
            current_way = way_check(way_change[0][1], current_way)
            way_change.popleft()

        if 0<=x<n and 0<=y<n and field[x][y]!=-1:
            queue.append((x, y))
            if field[x][y]==1: # 사과가 있는 경우
                field[x][y]=-1
            elif field[x][y]==0: # 그냥 빈칸 -> 꼬리줄인다.
                tail_x, tail_y = queue.popleft()
                field[tail_x][tail_y] = 0
                field[x][y]=-1
        else:
            break
    return second

n = int(input())
field=[[0]*n for _ in range(n)]
k = int(input()) # 사과갯수
# 사과 위치
for i in range(k):
    x, y = map(int, input().split())
    field[x-1][y-1] = 1
l = int(input()) # 방향 변화 횟수
way_change=deque()
for i in range(l):
    second, way = map(str, input().split())
    second = int(second)
    way_change.append((second, way))
print(snake_move(0))