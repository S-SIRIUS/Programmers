# 줄세우기
from collections import deque
import sys
input = sys.stdin.readline

def ts():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        node  = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1
ts()