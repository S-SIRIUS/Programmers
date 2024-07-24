from collections import defaultdict
import heapq

answer=[]
def dfs(airport, graph):
    global answer
    while graph[airport]:
        new_airport=heapq.heappop(graph[airport])
        dfs(new_airport, graph)
    answer.append(airport)
    
    
def solution(tickets):
    global answer
    graph = defaultdict(list)
    
    for start, end in tickets:
        heapq.heappush(graph[start], end)
        
    dfs("ICN", graph)
    
    
    return answer[::-1]