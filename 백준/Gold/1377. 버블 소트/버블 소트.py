# 버블 소트(골드2)
import sys
input = sys.stdin.readline
n = int(input())
array=[]
for i in range(n):
    array.append((int(input()), i+1))

array.sort(key = lambda x: x[0])
new_array=[]
for i in range(n):
    new_array.append(array[i][1] - (i+1) + 1)
print(max(new_array))