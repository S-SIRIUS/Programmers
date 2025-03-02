# 숨바꼭질4(골드4)
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def check_parent(x):
    
    answer_array.append(x)
    if x==n:
        return answer_array
    else:
        check_parent(parent[x])

def bfs():
    queue = deque()
    queue.append((n,0))
    visited[n]=1
    answer_time=0
    while queue:
        node, second = queue.popleft()

        if node == k:
            answer_time=second
            break
        else:
            if n  > k:
                c = node-1
                if 0<=c<=100000 and visited[c]==0:
                    queue.append((c, second+1))
                    parent[c]=node
                    visited[c]=1
    
            else:
                c1 = node+1
                if 0<=c1<=100000 and visited[c1]==0:
                    queue.append((c1, second+1))
                    parent[c1]=node
                    visited[c1]=1
                
                c2 = node-1
                if 0<=c2<=100000 and visited[c2]==0:
                    queue.append((c2, second+1))
                    parent[c2]=node
                    visited[c2]=1
                
                c3 = node*2
                if 0<=c3<=100000 and visited[c3]==0:
                    queue.append((c3, second+1))
                    parent[c3]=node
                    visited[c3]=1

    return answer_time

input = sys.stdin.readline
n, k = map(int, input().split())
visited=[0]*(100001)
parent=[0]*(100001)
a = bfs()
print(a)
answer_array=[]
check_parent(k)
for i in range(len(answer_array)-1, -1, -1):
    print(answer_array[i], end=" ")