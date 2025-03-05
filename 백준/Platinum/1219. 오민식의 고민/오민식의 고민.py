# 오민식의 고민(플래5)
import sys
input = sys.stdin.readline
inf = sys.maxsize
def bf(start):
    distances[start]=node_value[start]

    for i in range(n+101):
        for j in range(m):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            
            if distances[cur] == -inf:
                continue
            elif distances[cur] == inf:
                distances[next] = inf  
            elif distances[next] < distances[cur]+(node_value[next] - cost):
                distances[next] = distances[cur]+(node_value[next]-cost)
                if i>=n-1:
                    distances[next] = inf

n, start, end, m = map(int, input().split())
edges=[]
distances=[-inf]*(n)
for i in range(m):
    a, b, value = map(int, input().split())
    edges.append((a, b, value))
node_value = list(map(int, input().split()))
bf(start)
if distances[end] == -inf:
    print("gg")
elif distances[end]==inf:
    print("Gee")
else:
    print(distances[end])