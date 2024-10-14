# 행성터널(플래5)
import sys
input = sys.stdin.readline

def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def cruscal():
    planet_way.sort()
    answer=0
    edge_count=0
    for pw in planet_way:
        if find(pw[1]) != find(pw[2]):
            union(pw[1], pw[2])
            answer+=pw[0]
            edge_count+=1
            if edge_count == n - 1:  # 조기 종료
                break
    return answer


n = int(input())
planets=[]
parent = [i for i in range(0, n)]

x_list=[]
y_list=[]
z_list=[]
for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((x,i))
    y_list.append((y,i))
    z_list.append((z,i))

x_list.sort()
y_list.sort()
z_list.sort()

planet_way=[]
for cur_list in x_list, y_list, z_list:
    for i in range(1, n):
        w1, a = cur_list[i-1]
        w2, b = cur_list[i]
        planet_way.append((abs(w1-w2), a, b))

print(cruscal())