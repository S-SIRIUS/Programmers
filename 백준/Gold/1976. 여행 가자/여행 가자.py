# 여행 계획 짜기
import sys
sys.setrecursionlimit(10**8)

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a< b:
        parent[b] = a
    else:
        parent[a] = b
    return

n = int(input())
m = int(input())
parent = [i for i in range(0, n+1)]
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
path = list(map(int, input().split()))

for i in range (0, n):
    for j in range(0, n):
        if graph[i][j]==1:
            union(i+1, j+1)
standard = find(path[0])
answer="YES"
for i in path:
    if standard!=find(i):
        answer="NO"
        break
print(answer)