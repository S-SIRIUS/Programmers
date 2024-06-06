def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    if parent[a] < parent[b]:
        parent[parent[b]] = parent[a]
    else:
        parent[parent[a]] = parent[b]
    
def solution(n, costs):
    
    parent = [i for i in range(0, n)]
    costs.sort(key = lambda x:x[2])
    
    print(costs)
    mst=[]
    for i in costs:
        node, neighbor, cost = i
        if find_parent(parent, node) != find_parent(parent, neighbor):
            union_parent(parent, node, neighbor)
            mst.append(cost)
            if(len(mst)==n-1):
                print(mst)
                break
    return sum(mst)