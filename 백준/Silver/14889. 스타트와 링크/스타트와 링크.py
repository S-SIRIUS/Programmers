from itertools import combinations

# 스타트와 링크(실버1)
n = int(input())
member_num = n//2
abilities=[]
for i in range(n):
    abilities.append(list(map(int, input().split())))
members= [i for i in range(0, n)]
min_Val=999
for comb in combinations(members, n//2):
    start = 0
    link=0
    r1 = comb
    r2 = set(members) - set(comb)
    
    # start의 합
    for i in combinations(r1, 2):
        start += abilities[i[0]][i[1]]
        start += abilities[i[1]][i[0]]

    # link의 합
    for i in combinations(r2, 2):
        link += abilities[i[0]][i[1]]
        link += abilities[i[1]][i[0]]
    
    min_Val = min(min_Val, abs(start-link))
print(min_Val)