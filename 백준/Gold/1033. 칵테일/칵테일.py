# 칵테일
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


def dfs(node):
    for i in graph[node]:
        if visited[i[0]]==False:
            new_graph[i[0]] = new_graph[node] * i[2] // i[1]
            visited[i[0]]=True
            dfs(i[0])
    return

n = int(input())
graph=[[] for _ in range(n)]
new_graph = [0] * (n)
visited = [False]*(n)
update = 1
for i in range(n-1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    update *= (p*q) // gcd(p,q)

new_graph[0] = update
visited[0]=True
dfs(0)
mgcd = new_graph[0]
for i in range(1, n):
    mgcd = gcd(new_graph[i], mgcd)

for i in range(0, len(new_graph)):
    new_graph[i] = int(new_graph[i] // mgcd)
print(*new_graph)