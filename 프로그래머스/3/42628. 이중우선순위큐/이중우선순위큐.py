import heapq
def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        o, num = operation.split()
        num = int(num)
        
        if o == 'I':
            heapq.heappush(heap, num)
        elif o =='D' and num == 1:
            if len(heap) != 0:
                maxi = max(heap)
                heap.remove(maxi)
        else:
            if len(heap) != 0:
                heapq.heappop(heap)
        
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
    return answer