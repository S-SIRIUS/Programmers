# N과M(3)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def backtrack(index):
    if index==m:
        print(*array)
        return
    else:
        for i in range(1, n+1):
            array.append(i)
            backtrack(index+1)
            array.pop()
    return

n, m = map(int, input().split())
array=[]
backtrack(0)