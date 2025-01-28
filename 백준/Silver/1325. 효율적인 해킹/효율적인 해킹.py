# 효율적으로 해킹하기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node]=True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i]==0:
                visited[i]=1
                reliability[i-1]+=1
                queue.append(i)
    return

n, m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

reliability=[0 for _ in range(n)]

for i in range(1, n+1):
    visited=[0 for _ in range(n+1)]
    bfs(i)

data = max(reliability)
for i in range(0, n):
    if reliability[i] == data:
        print(i+1, end=" ")