# 트리의 지름(골드4)
import sys
sys.setrecursionlimit(10**6)

def dfs(n, value):
    visited[n]=True
    max_n = n
    max_val = value
    for i in graph[n]:
        if visited[i[0]]==False:
            current_n, current_val = dfs(i[0], value+i[1])
            if current_val > max_val:
                max_n = current_n
                max_val = current_val
    return max_n, max_val


input = sys.stdin.readline
n = int(input().strip())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(n-1):
    parent, child, value = map(int, input().split())
    graph[parent].append((child, value))
    graph[child].append((parent, value))
node1, value1 = dfs(1, 0)
visited=[False]*(n+1)
node2, value2 = dfs(node1, 0)
print(value2)