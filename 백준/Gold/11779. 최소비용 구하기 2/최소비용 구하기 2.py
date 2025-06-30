# 최소비용(골드3)
import heapq
inf = int(1e9)
n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())

distance = [inf] * (n + 1)
prev = [0] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            if distance[next_node] > dist + cost:
                distance[next_node] = dist + cost
                prev[next_node] = now
                heapq.heappush(q, (distance[next_node], next_node))

dijkstra(start)

path = []
cur = end
while cur != 0:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(distance[end])
print(len(path))
print(' '.join(map(str, path)))