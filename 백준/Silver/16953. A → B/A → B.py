# A -> B(실버2)
import sys
from collections import deque

def bfs(iv, target):
    queue= deque()
    count=0
    queue.append((iv, count))

    while queue:
        p, count = queue.popleft()
        if p == target:
            return count
        
        elif p < target:
            new_p1 = p*2
            count+=1
            new_p2 = int(str(p) + "1")
            queue.append((new_p1, count))
            queue.append((new_p2, count))
    return -2

input = sys.stdin.readline


a, b = map(int, input().split())
print(bfs(a,b)+1)