# 특정한 최단 경로(골드4)
import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

n, e = map(int, input().split())
graph=[[] for _ in range(n+1)]
distances=[inf] * (n+1)
for i in range(e):
    a, b, c =map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

must = list(map(int, input().split()))

def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0, start))
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
                    heapq.heappush(queue,(cost, i[0]))

way1=0
way2=0
dijkstra(1)
way1+=distances[must[0]]
way2+=distances[must[1]]

distances=[inf] * (n+1)
dijkstra(must[0])
way1+=distances[must[1]]
way2+=distances[n]

distances=[inf] * (n+1)
dijkstra(must[1])
way1+=distances[n]
way2+=distances[must[0]]

if way1 >= inf or way2 >= inf:
    print(-1)
else:
    print(min(way1,way2))