# N과 M(실버3)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def backtrack(now, index):
    if index==m:
        print(*array)
    else:
        element[now]=1
        for e in range(1, n+1):
            if element[e]!=1:
                array.append(e)
                backtrack(e, index+1)
                array.pop()
        element[now]=0

n, m = map(int, input().split())
array=[]
element = [0]*(n+1)
for i in range(1, n+1):
    array.append(i)
    backtrack(i, 1)
    array.pop()