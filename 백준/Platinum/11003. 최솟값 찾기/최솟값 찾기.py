# 최솟값 찾기1(플래티넘5)
from collections import deque
n, win_size = map(int, input().split())
data = list(map(int, input().split()))
queue = deque()

for i in range(0, n):

    while queue and queue[-1][0] > data[i]:
        queue.pop()
    
    queue.append((data[i], i))

    if i-queue[0][1] >= win_size:
        queue.popleft()
    
    print(queue[0][0], end=" ")