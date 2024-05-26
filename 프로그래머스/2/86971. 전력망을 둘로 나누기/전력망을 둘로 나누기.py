
def dfs(new_wire, i, n, visited):
    count=1
    visited[i]=True
    for j in new_wire[i]:
        if not visited[j]:
            count += dfs(new_wire, j, n, visited)
    return count

def solution(n, wires):
    ans=[]
    temp_wires= wires.copy()
    
    for w in wires:
        counts=[]
        visited = [False] * (n+1)
        temp_wires.remove(w)
        new_wire=[[] for _ in range(n+1)]
        
        for wire in temp_wires:
            if wire[1] not in new_wire[wire[0]]:
                new_wire[wire[0]].append(wire[1])
            if wire[0] not in new_wire[wire[1]]:
                new_wire[wire[1]].append(wire[0])

        for i in range(1, n+1):
            if visited[i] == False:
                count = dfs(new_wire, i, n, visited)
                counts.append(count)
        ans.append(abs(counts[0] - counts[1]))
        temp_wires.append(w)
        
    return min(ans)