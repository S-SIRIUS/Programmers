# 마인크래프트(실버2)
import sys
n, m, b = map(int, input().split())
table = []
for i in range(n):
    table.append(list(map(int, sys.stdin.readline().rstrip().split())))

ans = 999999999999999
ans_height=0

for i in range(0, 257):
    u_block=0
    t_block=0
    for j in range(n):
        for k in range(m):
            if i > table[j][k]:  # 블록을 쌓아야 하는 경우
                u_block += i - table[j][k]
            elif i < table[j][k]:  # 블록을 제거해야 하는 경우
                t_block += table[j][k] - i
            # 인벤토리 블록이 부족한 경우나 초과하는 경우를 확인
    if u_block > t_block+b:
        continue
    time = u_block + t_block*2

    if time <= ans:
        ans = time
        ans_height = i
print(ans, ans_height)