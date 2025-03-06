# N과M(7) (실버3)
import sys
input = sys.stdin.readline
def backtrack(index):
    if index==m:
        print(*array)
        return
    else:
        for i in candidates:
            array.append(i)
            backtrack(index+1)
            array.pop()
    return
n, m = map(int ,input().split())
candidates = list(map(int, input().split()))
candidates.sort()
array=[]
backtrack(0)