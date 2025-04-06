import heapq
inf = int(1e9)
def dijkstra(start, distances, graph):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start]=0
    while queue:
        now_distance, now_node = heapq.heappop(queue)
        if now_distance > distances[now_node]:
            continue
        else:
            for next_value in graph[now_node]:
                next_node = next_value[0]
                next_distance = next_value[1]
                if distances[next_node] > now_distance+next_distance:
                    distances[next_node] = now_distance+next_distance
                    heapq.heappush(queue, (now_distance+next_distance, next_node))
    return distances
    


def solution(n, s, a, b, fares):
    answer = 0
    graph=[[]for _ in range(n+1)]
    distances=[inf]*(n+1)
    
    for f in fares:
        graph[f[0]].append((f[1], f[2]))
        graph[f[1]].append((f[0], f[2]))
    distances = dijkstra(s, distances, graph)
    
    cases = [i for i in range(1, n+1)]
    cases.remove(s)
    candidates=[]
    candidates.append(distances[a]+distances[b])
    for case in cases:
        temp_distances=[inf]*(n+1)
        temp_distances = dijkstra(case, temp_distances, graph)
        candidates.append(distances[case]+temp_distances[a]+temp_distances[b])
    answer = min(candidates)
    return answer