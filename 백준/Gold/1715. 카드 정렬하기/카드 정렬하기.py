import heapq
n = int(input())
card = []
total=0
for i in range(n):
    heapq.heappush(card, int(input()))


while len(card)>1:
    a1 = heapq.heappop(card)
    a2 = heapq.heappop(card)
    compare=(a1+a2)
    heapq.heappush(card, compare)
    total+=compare
print(total)