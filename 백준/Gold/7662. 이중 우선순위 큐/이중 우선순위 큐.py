import heapq

t = int(input().strip())
for _ in range(t):
    k = int(input().strip())
    
    min_heap = []
    max_heap = []
    entry_map = {}  # 각 요소의 삽입 상태를 추적하기 위한 맵

    for _ in range(k):
        o, n = input().split()
        n = int(n)

        if o == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            if n in entry_map:
                entry_map[n] += 1
            else:
                entry_map[n] = 1
        elif o == "D":
            if n == -1: 
                while min_heap and entry_map[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    smallest = heapq.heappop(min_heap)
                    entry_map[smallest] -= 1
            elif n == 1:  
                while max_heap and entry_map[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)  
                if max_heap:
                    largest = -heapq.heappop(max_heap)
                    entry_map[largest] -= 1


    while min_heap and entry_map[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_map[-max_heap[0]] == 0:
        heapq.heappop(max_heap)


    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")