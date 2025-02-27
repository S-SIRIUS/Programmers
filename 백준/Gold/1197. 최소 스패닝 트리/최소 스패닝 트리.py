# 최소 스패닝 트리(골드4)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a< b:
        parent[b] = a
    else:
        parent[a] =b
    return

n, e = map(int, input().split())
parent=[i for i in range(0, n+1)]
rank = [0] * (n + 1) 
edges=[]
for i in range(e):
    a, b, v = map(int, input().split())
    edges.append((v, a, b))
edges.sort()
answer=0
for edge in edges:
    v, a, b = edge
    if find(a)!=find(b):
        union(a,b)
        answer+=v
print(answer)