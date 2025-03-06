# 애너그램(골드5)
import sys
from collections import Counter
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def backtrack(index):
    if index==m:
        candidate= "".join(array)
        print(candidate)
        return
    else:
        for i in duplicate:
            if duplicate[i]>0:
                array.append(i)
                duplicate[i]-=1
                backtrack(index+1)
                array.pop()
                duplicate[i]+=1
n = int(input().strip())
for i in range(n):
    data = list(input().strip())
    m = len(data)
    data.sort()
    array=[]
    duplicate=Counter(data)
    backtrack(0)