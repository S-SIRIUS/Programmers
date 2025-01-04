# 나머지 합 구하기(골드3)
from collections import Counter
answer=0
n, m = map(int, input().split())
field = list(map(int, input().split()))
for i in range(1, n):
    field[i] += field[i-1]
for i in range(0, n):
    field[i] = (field[i] % m)
    if field[i]==0:
        answer+=1
field_c = Counter(field)

for key in field_c:
    if field_c[key] > 1:
        answer += field_c[key]*(field_c[key]-1)//2
print(answer)