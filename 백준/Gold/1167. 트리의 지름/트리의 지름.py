# 트리의 지름(골드2)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, value):
    visited[node]=True
    max_node = node
    max_value = value
    for i in graph[node]:
        if visited[i[0]]==False:
            current_node, current_value = dfs(i[0], value+i[1])
            if current_value > max_value:
                max_value = current_value
                max_node = current_node
    return max_node, max_value

n = int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(n):
    node, *list_info = map(int, input().split())
    for j in range(0, len(list_info), 2):
        if list_info[j]==-1:
            break
        graph[node].append((list_info[j], list_info[j+1]))

node1, value1 = dfs(1, 0)
visited=[False]*(n+1)
node2, value2 = dfs(node1, 0)
print(value2)