# 치킨배달(골드5)
from itertools import combinations


def choose_short(candidate):
    global house
    global minimum_candidate
    minimum=1e9
    summ=0
    for j in house:
        minimum=1e9
        for i in candidate:
            value = abs(i[0] - j[0]) + abs(i[1]-j[1])
            if value < minimum:
                minimum=value
        summ+=minimum
    minimum_candidate.append(summ)
    return
    
n, m = map(int, input().split())
field=[]
chicken=[]
house=[]
for i in range(n):
    field.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if field[i][j]==2:
            chicken.append((i,j))
        elif field[i][j]==1:
            house.append((i,j))
minimum_candidate=[]
candidates = list(combinations(chicken, m))
for candidate in candidates:
    choose_short(candidate)
print(min(minimum_candidate))