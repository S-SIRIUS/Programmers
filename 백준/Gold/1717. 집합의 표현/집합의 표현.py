import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
        return parent[x]
    else:
        return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

def check(a, b):
    if find(a)==find(b):
        return "YES"
    else:
        return "NO"
n, m = map(int, input().split())
parent = [i for i in range(0, n+1)]
for i in range(m):
    op, a, b = map(int, input().split())
    if op==0:
        union(a,b)
    else:
        print(check(a,b))