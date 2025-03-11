# 회전초밥(실버1)
import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
chobap = []
for i in range(n):
    chobap.append(int(input()))
chobap += chobap
answer=-999
for i in range(0, len(chobap)//2):
    data = chobap[i:i+k]
    candidate = len(set(data))
    if c not in data:
        candidate +=1
    answer = max(answer, candidate)
print(answer)