# 다리만들기(골드1)
from collections import deque
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def garo():
    for standard in range(n):
        a=0
        b=0
        count=0
        flag=0
        for j in range(m):
            if flag==1 and field[standard][j]==0:
                count+=1
            
            # 초기 a 설정 flag로 count 시작
            if field[standard][j]!=0 and a==0:
                a=field[standard][j]
                flag=1
            
            if field[standard][j]!=0 and field[standard][j]==a:
                count=0 
            elif field[standard][j]!=0 and field[standard][j]!=a:
                b = field[standard][j]
                if count > 1:
                    storage[-a][-b] = min(storage[-a][-b], count)
                    storage[-b][-a] = min(storage[-b][-a], count)
                a = b
                count=0

    return

def sero():
    for j in range(m):
        a=0
        b=0
        count=0
        flag=0
        for standard in range(n):
            if flag==1 and field[standard][j]==0:
                count+=1
            if field[standard][j]!=0 and a==0:
                a=field[standard][j]
                flag=1
            if field[standard][j]!=0 and field[standard][j]==a:
                count=0 
            elif field[standard][j]!=0 and field[standard][j]!=a:
                b = field[standard][j]
                if count > 1:
                    storage[-a][-b] = min(storage[-a][-b], count)
                    storage[-b][-a] = min(storage[-b][-a], count)
                a = b
                count=0
    return


def change(i, j, group):
    queue = deque()
    queue.append((i,j))
    field[i][j]=group

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(0, 4):
            new_x  = now_x + dx[i]
            new_y = now_y + dy[i]

            if 0<=new_x<n and 0<=new_y<m and field[new_x][new_y]==1:
                field[new_x][new_y]=group
                queue.append((new_x, new_y))

    return

def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return
n, m = map(int, input().split())
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))

group=-1
for i in range(n):
    for j in range(m):
        if field[i][j]==1:
            change(i,j, group)
            group-=1
inf = int(1e9)
storage=[[inf]*(-group) for _ in range(-group)]
garo()
sero()
distances=[]
for i in range(1, -group):
    for j in range (1, -group):
        if storage[i][j] != inf:
           if (storage[i][j], i, j) not in distances and (storage[i][j], j, i) not in distances:
            distances.append((storage[i][j], i, j))
parent = [i for i in range(-(group))]
distances.sort()
answer=0
b_count=0
for d in distances:
    node1 = -d[1]
    node2 = -d[2]
    if find(node1) != find(node2):
        union(node1, node2)
        answer+=d[0]
        b_count+=1
if (-group)-1 == 1:
    print(0)
elif b_count < (-group-1)-1:
    print(-1)
else:
    print(answer)