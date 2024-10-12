# 도시분할계획(골드4)
import sys
input = sys.stdin.readline
def find(x):
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return


n, m = map(int, input().split())
edges=[]
parents=[i for i in range(0, n+1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

summ=0
last=0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a,b)
        summ+=cost
        last=cost
print(summ-last)