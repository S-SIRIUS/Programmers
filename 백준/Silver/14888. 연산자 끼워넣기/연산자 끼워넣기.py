# 연산자 끼워 넣기(실버1)
import sys
input = sys.stdin.readline

max_val = -1e9
min_val = 1e9

def dfs(depth, value, plus, minus, multiply, divide):
    global max_val, min_val

    if depth == n:
        max_val = max(value, max_val)
        min_val = min(value, min_val)
        return
    
    if plus:
        dfs(depth+1, value + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, value - nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, value * nums[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(value / nums[depth]), plus, minus, multiply, divide-1)




n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

dfs(1, nums[0], operators[0], operators[1], operators[2], operators[3])

print(max_val)
print(min_val)