#케빈 베이컨의 6단계 법칙(실버1)
from collections import deque
summ=0
def bfs(standard):
    global check_table
    queue = deque()
    queue.append(standard)
    check_table[standard]=0
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if(check_table[i]==-1):
                check_table[i] = check_table[value]+1
                queue.append(i)
    return sum(check_table)+1

n, m = map(int, input().split())
target_value=[0]*(n+1)
graph=[[]for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    check_table=[-1]*(n+1)
    target_value[i]+= bfs(i)
target_value[0]=99999999999999999999999999999
print(target_value.index(min(target_value)))