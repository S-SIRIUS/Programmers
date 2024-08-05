dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def rotation(direction):
    if direction==0:
        direction =3
    else:
        direction-=1
    return direction

def direction_forward(direction, x, y):
    if direction==0:
        x-=1
    elif direction==1:
        y+=1
    elif direction==2:
        x+=1
    else:
        y-=1
    return x, y

def direction_validation(x, y, rooms):
    global n, m 
    if 0<=x<n and 0<=y<m and rooms[x][y]!=1:
        return True
    else:
        return False

def direction_backward(direction, x, y):
    if direction==0:
        x+=1
    elif direction==1:
        y-=1
    elif direction==2:
        x-=1
    else:
        y+=1
    return x, y


def simulation(x, y, rooms, direction):
    global count
    while True:
        if rooms[x][y]==0:
            rooms[x][y]=2
            count+=1
        empty=0
        for i in range(0, 4):
            new_x=x+dx[i]
            new_y=y+dy[i]
            if rooms[new_x][new_y] == 0:
                empty=1
        if empty==0:
            # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
            temp_x, temp_y = direction_backward(direction, x, y)
            if (direction_validation(temp_x, temp_y, rooms)):
                x = temp_x
                y = temp_y
                continue
            else:
                break
        else:
            # 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
            direction = rotation(direction)
            temp_x, temp_y = direction_forward(direction, x, y)
            if (direction_validation(temp_x, temp_y, rooms)):
                if rooms[temp_x][temp_y]==0:
                    x= temp_x
                    y= temp_y
                

n, m = map(int, input().split())
rooms=[]
start_x, start_y, direction = map(int, input().split())
for i in range(n):
    rooms.append(list(map(int, input().split())))
count=0
simulation(start_x, start_y, rooms, direction)
print(count)