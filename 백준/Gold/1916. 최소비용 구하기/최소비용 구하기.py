# 최소비용 구하기(골드5)
import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

n = int(input())
m = int(input())

graph=[[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
question = list(map(int,input().split()))
distances=[inf]*(n+1)

def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    while queue:
        distance, node = heapq.heappop(queue)
        if distances[node] < distance:
            continue
        else:
            for i in graph[node]:
                cost = distance+ i[1]
                if cost < distances[i[0]]:
                    distances[i[0]] = cost
                    heapq.heappush(queue,(cost,i[0]))
dijkstra(question[0])
print(distances[question[1]])        