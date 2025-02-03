# 물통(골드5)
import sys
from collections import deque
input = sys.stdin.readline

def pour(x, y):
    if not visited[x][y]:
        visited[x][y]=True
        queue.append((x, y))

def bfs():
    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x==0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x-water,y+water)

        # x -> z
        water = min(x, c-z)
        pour(x-water, y)
        
        # y -> x
        water = min(y, a-x)
        pour(x+water, y-water)

        # y -> z
        water = min(y, c-z)
        pour(x, y-water)

        # z -> x
        water = min(z, a-x)
        pour(x+water, y)

        # z -> y
        water = min(z, b-y)
        pour(x, y+water)


a, b, c = map(int, input().split())
visited=[[False for _ in range(b+1)] for _ in range(a+1)]
answer=[]
queue = deque()
queue.append((0, 0))
visited[0][0]=True
bfs()
answer.sort()
print(*answer)