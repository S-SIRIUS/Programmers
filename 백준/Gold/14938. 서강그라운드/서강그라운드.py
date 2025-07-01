# 서강 그라운드(골드4)
import sys
import heapq
inf = float(1e9)
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1].append((b-1, l))
    graph[b-1].append((a-1, l))

def dijkstra(start):
    dist = [inf] * n
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    
    while hq:
        cost, now = heapq.heappop(hq)
        if dist[now] < cost:
            continue
        for next_node, weight in graph[now]:
            if dist[next_node] > cost + weight:
                dist[next_node] = cost + weight
                heapq.heappush(hq, (dist[next_node], next_node))
    return dist

max_items = 0

for i in range(n):
    dist = dijkstra(i)
    total = 0
    for j in range(n):
        if dist[j] <= m:
            total += items[j]
    max_items = max(max_items, total)

print(max_items)