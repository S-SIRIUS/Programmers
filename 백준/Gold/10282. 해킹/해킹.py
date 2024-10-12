# 해킹(골드4)

import heapq
import sys
input = sys.stdin.readline
inf= int(1e9)

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
                cost = distance+ i[1]
                if distances[i[0]] > cost:
                    distances[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
   
    counts=0
    for i in range(n+1):
        if distances[i]<inf:
            counts+=1
        else:
            distances[i]=-999
    last_com = max(distances)
    return counts, last_com

tcases = int(input())
for tcase in range(tcases):
    n, d, c = map(int, input().split())
    distances = [inf]*(n+1)
    graph=[[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))
    counts, last_com = dijkstra(c)
    print(counts, last_com)