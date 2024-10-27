# 웜홀(골드3)
import sys
input = sys.stdin.readline
INF = int(1e9)
def bf():
    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if distances[next] > distances[cur] + cost:
                distances[next] = distances[cur] + cost
                if i == n-1:
                    return True
    return False

        
tc = int(input())
for i in range(tc):
    n, m, w = map(int, input().split())
    edges=[]
    distances = [INF] * (n+1)
    for i in range(m + w):
        s, e, t = map(int, input().split())
        if i >= m:
            t = -t
        else:
            edges.append((e,s,t))
        edges.append((s,e,t))
    if bf():
        print("YES")
    else:
        print("NO")