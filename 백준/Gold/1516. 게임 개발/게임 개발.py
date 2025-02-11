# 게임 개발하기(골드3)
import sys
from collections import deque
input = sys.stdin.readline

def ts():
    queue = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            answer[i] = values[i]
            queue.append(i)
    
    while queue:
        new_node = queue.popleft()
        for next_node in graph[new_node]:
            answer[next_node] = max(answer[next_node], answer[new_node] + values[next_node])
            indegree[next_node]-=1
            if indegree[next_node]==0:
                queue.append(next_node)
    return

n = int(input())
indegree = [0]*(n+1)
graph=[[] for _ in range(n+1)]
values=[0]*(n+1)
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    values[i]=temp[0]
    indegree_list = temp[1:-1]
    indegree[i]=len(indegree_list)
    for j in indegree_list:
        graph[j].append(i)
answer=[0]*(n+1)
ts()
for i in range(1, n+1):
    print(answer[i])