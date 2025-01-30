import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
def dfs(i,label):
    visited[i]=label

    for j in graph[i]:
        if not visited[j]:
            a=dfs(j,-label)
            if(a==False):
                return False
        else:
            if(visited[j]==visited[i]):
                return False
        

a=int(input())
for i in range(a):
    b,c = map(int, input().split())
    graph=[[] for _ in range(b+1)]
    for j in range(c):
        m,n=map(int,input().split())
        graph[m].append(n)
        graph[n].append(m)
    visited=[False]*(b+1)
    for k in range(1,b+1):
        if not visited[k]:
            l=dfs(k,1)
            if(l==False):
                break
    if(l==False):
        print("NO")
    else:
        print("YES")