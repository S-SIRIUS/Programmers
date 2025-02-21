# 임계경로(플래5)
import sys
from collections import deque
input = sys.stdin.readline

def ts():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            queue.append(i)
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            new_node = i[0]
            new_value = i[1]
            indegree[new_node]-=1
            dp[new_node] = max(dp[new_node], dp[now_node]+ new_value)
            if indegree[new_node]==0:
                queue.append(new_node)
    return

def rts():
    queue = deque()
    visited=[0]*(n+1)
    queue.append(end)
    visited[end]=1
    answer=0
    while queue:
        now_node = queue.popleft()
        for i in graph2[now_node]:
            new_node = i[0]
            new_value = i[1]
            indegree2[new_node]-=1
            if (dp[now_node] - new_value) == dp[new_node]:
                answer+=1
                if visited[new_node]==0:
                    queue.append(new_node)
                    visited[new_node]=1
    return answer
n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]
graph2=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
indegree2=[0]*(n+1)
dp=[0]*(n+1)
for i in range(m):
    a, b, value = map(int, input().split())
    graph[a].append((b, value))
    graph2[b].append((a, value))
    indegree[b]+=1
    indegree2[a]+=1

start, end = map(int, input().split())
ts()
print(dp[end])
answer = rts()
print(answer)