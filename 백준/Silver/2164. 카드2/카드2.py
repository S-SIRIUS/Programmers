# 카드2(실버4)
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)
print(queue[0])