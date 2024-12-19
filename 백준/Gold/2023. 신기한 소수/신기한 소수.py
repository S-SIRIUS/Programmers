# 신기한 소수찾기(골드5)
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
def check_prime(num):
    for i in range(2, num//2):
        if num % i==0:
            return False
    return True
def dfs(num, count):
    if count == n:
        print(num)
        return
    else:
        for i in (1, 3, 5, 7, 9):
            if check_prime(num*10 + i):
                dfs(num*10 + i, count+1)
    return
n = int(input())
for i in (2, 3, 5, 7):
    dfs(i, 1)
