# K번째 최단경로 찾기
import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

def dijkstra(start):
    queue=[]
    heapq.heappush(queue, (0, start))
    visited[1][0]=0

    while queue:
        now_value, now_node = heapq.heappop(queue)

        for next_node, next_value in graph[now_node]:
            cost = now_value+next_value
            if cost < visited[next_node][k-1]:
                visited[next_node][k-1] = cost
                visited[next_node].sort()
                heapq.heappush(queue, (cost, next_node))
    return


n, m, k = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))

visited=[[inf]*(k) for _ in range(n+1)]
dijkstra(1)
for i in range(1, n+1):
    if visited[i][k-1]==inf:
        print(-1)
    else:
        print(visited[i][k-1])