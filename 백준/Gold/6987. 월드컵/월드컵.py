# 월드컵(골드4)
import sys
from itertools import combinations
def backtrack(index):
    global answer
    if index==15:
        for i in new_table:
            if i.count(0)!=3:
                return
        answer=1
        return
    else:
        t1, t2 = cs[index]
        for x, y in ((0,2), (1, 1), (2, 0)):
            if new_table[t1][x] >0 and new_table [t2][y]>0:
                new_table[t1][x]-=1
                new_table[t2][y]-=1
                backtrack(index+1)
                new_table[t1][x]+=1
                new_table[t2][y]+=1


input = sys.stdin.readline
r_answer=[]
player = [i for i in range(0, 6)]
cs = list(combinations(player, 2))
for i in range(4):
    table = list(map(int, input().split()))
    new_table=[]
    storage_index=0
    answer=0
    for i in player:
        new_table.append(table[storage_index:storage_index+3])
        storage_index+=3
    backtrack(0)
    r_answer.append(answer)
print(*r_answer)