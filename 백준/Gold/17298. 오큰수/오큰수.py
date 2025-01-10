# 오큰 수 구하기(골드4)
import sys
input = sys.stdin.readline
n = int(input())
array= list(map(int, input().split()))
answer=[-1]*(n)
stack=[]
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= array[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1]
    stack.append(array[i])
print(*answer)