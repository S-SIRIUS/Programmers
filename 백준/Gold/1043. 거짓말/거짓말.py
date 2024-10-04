# 거짓말(골드 4)
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
node = [i for i in range(0, n+1)]
true_list = list(map(int, input().split()))[1:]
parent = [i for i in range(n+1)]

for i in true_list:
    union(0, i)

parties=[]
for i in range(m):
    cnt, *party = list(map(int, input().split()))
    parties.append(party)
    for i in range(cnt-1):
        union(party[i], party[i+1])

answer=0
for party in parties:
    if find(party[0]) == 0:
        continue
    answer+=1
print(answer)