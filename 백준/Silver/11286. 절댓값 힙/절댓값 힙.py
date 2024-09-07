import heapq
import sys
heap=[]
n = int(input())
for i in range(n):
    value = int(sys.stdin.readline().strip())
    if value==0:
        if not heap:
            print(0)
        else:
            answer = heapq.heappop(heap)
            print(answer[1])
    
    else:
        heapq.heappush(heap, (abs(value),value))