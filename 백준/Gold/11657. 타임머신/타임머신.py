# 타임머신(골드4)
import sys
input = sys.stdin.readline
inf = (1e9)

def bf(start):
    distances[start]=0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next = edges[j][1]
            value = edges[j][2]

            if distances[cur]!=inf and distances[next] > distances[cur]+value:
                distances[next] = distances[cur]+value
                if i==n-1:
                    return True
    return False


n, m = map(int, input().split())
distances=[inf]*(n+1)
edges = []
for i in range(m):
    a, b, value = map(int, input().split())
    edges.append((a, b, value))
if bf(1):
    print(-1)
else:
    for i in range(2, n+1):
        if distances[i]==inf:
            print(-1)
        else:
            print(distances[i])