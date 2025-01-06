# 좋다(골드4)
import sys
input = sys.stdin.readline
n = int(input())
field = list(map(int, input().split()))
field.sort()
answer=0
for i in range(0, n):
    start=0
    end=n-1
    while start < end:
        if field[start] + field[end] == field[i]:
            if start!=i and end!=i:
                answer+=1
                break
            elif start==i:
                start+=1
            else:
                end-=1
        elif field[start] + field[end] < field[i]:
            start+=1
        else:
            end-=1
print(answer)