def dfs(n_computers, i, visited):
    if visited[i] == True:
        return
    else:
        visited[i] = True
    
        for node in n_computers[i]:
            dfs(n_computers, node, visited)
    
    return
def solution(n, computers):
    answer = 0
    
    n_computers=[[] for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if computers[i][j] == 1 and i!=j:
                n_computers[i].append(j)
    
    visited = [False]*n
    for i in range(0, n):
        if visited[i] == False:
                answer+=1
                dfs(n_computers, i, visited)
        
    return answer