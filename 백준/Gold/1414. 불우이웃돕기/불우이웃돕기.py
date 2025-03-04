# 불우이웃돕기(골드3)
import sys
input = sys.stdin.readline

def exchange(alphabet):
    if ord('a') <=ord(alphabet) <= ord('z'):
        return ord(alphabet)- ord('a')+1
    elif ord('A') <= ord(alphabet) <= ord('Z'):
        return ord(alphabet) - ord('A')+27
    
    return 0
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

n = int(input())
edges=[]
total=0
parent = [i for i in range(n+1)]
for i in range(n):
    temp = list(input())
    for j in range(n):
        temp_value = exchange(temp[j])
        total+=temp_value
        if j!=i and temp_value!=0:
            edges.append((temp_value, i+1, j+1))
edges.sort()
need=0
for e in edges:
    value, n1, n2 = e
    if find(n1)!=find(n2):
        union(n1, n2)
        need+=value
iv=parent[1]
for i in range(2, n+1):
    if iv!= find(i):
        print(-1)
        sys.exit(0)
print(total-need)