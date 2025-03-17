# DNA(실버4)
import sys
from collections import Counter

n, m = map(int, input().split())
str_list=[]
for i in range(n):
    str_list.append(input())
new_list=[[] for _ in range(m)]
for i in range(m):
    for j in range(n):
        new_list[i].append(str_list[j][i])
new_str=""
answer=0
for i in range(m):
    c = Counter(new_list[i])
    sorted_items = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    c= dict(sorted_items)
    for key in c:
        answer+=(n-c[key])
        new_str+=key
        break
print(new_str)
print(answer)