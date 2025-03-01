# 숨바꼭질2(골드4)
import sys
from collections import deque
inf = int(1e9)
def bfs():
    queue = deque()
    queue.append((start,0))
    answer_time=-1
    ways=0
    
    while queue:
        node, second = queue.popleft()
        if ways>0 and second != answer_time:
            break
        else:
            if node == target:
                answer_time = second
                ways+=1
        
        new_node_1 = node-1
        if 0<=new_node_1<=100000:
            if dp[new_node_1] >= second+1:
                dp[new_node_1] = second+1
                queue.append((new_node_1, dp[new_node_1]))

        new_node_2 = node+1
        if 0<=new_node_2<=100000:
            if dp[new_node_2] >= second+1:
                dp[new_node_2] = second+1
                queue.append((new_node_2, dp[new_node_2]))

        new_node_3 = node*2
        if 0<=new_node_3<=100000:
            if dp[new_node_3] >= second+1:
                dp[new_node_3] = second+1
                queue.append((new_node_3, dp[new_node_3]))
    
    return answer_time, ways

input = sys.stdin.readline
start, target = map(int, input().split())
dp=[inf]*(100001)
a, b = bfs()
print(a)
print(b)