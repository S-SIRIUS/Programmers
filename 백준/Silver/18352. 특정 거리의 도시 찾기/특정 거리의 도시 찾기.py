# 이코테 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline
answer=[]
def bfs(X):
    queue = deque()
    queue.append((X, 0))
    visited[X]=True
    while queue:
        next, distance = queue.popleft()
        
        if distance==K:
            answer.append(next)

        for i in graph[next]:
            if visited[i]==False:
                visited[i]=True
                queue.append((i, distance+1))
    return

N, M, K, X = map(int, input().split())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
bfs(X)

if len(answer)==0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)