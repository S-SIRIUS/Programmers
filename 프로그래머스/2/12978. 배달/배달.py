import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

def solution(N, road, K):
    answer = 0
    graph=[[] for _ in range(N+1)]
    
    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
    
    distances=[inf]*(N+1)
    

    def dijkstra(start):
        queue=[]
        heapq.heappush(queue, (0, start))
        distances[start]=0
        while queue:
            distance, node = heapq.heappop(queue)
            
            if distances[node] < distance:
                continue
                
            for i in graph[node]:
                cost = distance + i[1]
                if cost < distances[i[0]]:
                    distances[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
  
    dijkstra(1)
  
    for i in distances:
        if i<=K:
            answer+=1
  
    return answer