# 회전초밥(실버1)
import sys
from collections import Counter
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
chobap = []
for i in range(n):
    chobap.append(int(input()))
chobap += chobap
chb = Counter(chobap[0:k])
answer=len(chb)
if c not in chb:
    answer+=1
for i in range(1, len(chobap)//2):
    chb[chobap[i-1]]-=1
    if chb[chobap[i-1]]==0:
        del chb[chobap[i-1]]
    
    chb[chobap[i+k-1]]+=1
    
    candidate = len(chb)
    if c not in chb:
        candidate +=1
    answer = max(answer, candidate)
print(answer)