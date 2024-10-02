# 최단경로(골드4)
import sys
import heapq

inf = (1e9)
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input().strip())
graph=[[] for _ in range(v+1)]
for i in range(e):
    a, b, c  = map(int, input().split())
    graph[a].append((b,c))
distances=[inf]*(v+1)

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
                    distances[i[0]]  = cost
                    heapq.heappush(queue, (cost, i[0]))
dijkstra(k)
for i in range(1, v+1):
    if distances[i] >= inf:
        print("INF")
    else:
        print(distances[i])