# 파티(골드3)
import heapq
import sys
input = sys.stdin.readline
inf = (1e9)

def dijkstra(start):
    queue=[]
    heapq.heappush(queue, (0, start))
    distances[start]=0

    while queue:
        distance, node = heapq.heappop(queue)
        if distances[node] < distance:
            continue
        else:
            for i in graph[node]:
                cost = distance + i[1]
                if cost < distances[i[0]]:
                    distances[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))


n, m, x = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

maxv=-999
for i in range(1, n+1):
    return_cost=0
    distances=[inf]*(n+1)
    dijkstra(i)
    return_cost += distances[x]
    distances=[inf]*(n+1)
    dijkstra(x)
    return_cost += distances[i]
    if return_cost > maxv:
        maxv = return_cost
print(maxv)