# 친구 관계 파악하기(골드5)
import sys
input = sys.stdin.readline
answer =0
def dfs(num, count):
    global answer
    if count == 5:
        answer = 1
        return
    else:
        visited[num]=True
        for i in graph[num]:
            if visited[i]==False:
                dfs(i, count+1)
        visited[num]=False
    return

n, e = map(int, input().split())
graph=[[] for _ in range(n)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n)
for i in range(n):
    dfs(i, 1)
    if answer == 1:
        print(answer)
        break
if answer!=1:
    print(answer)