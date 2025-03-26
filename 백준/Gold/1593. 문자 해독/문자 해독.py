# 문자해독(골드5)
from collections import Counter
n, m = map(int, input().split())
w = list(input())
s= list(input())
start=0
end=n
standard = Counter(w)
answer=0
comp = Counter(s[start:end])

flag=1
for key in standard:
    if standard[key]!=comp[key]:
        flag=0
        break
if flag==1:
    answer+=1

while end<m:
    flag=1
    comp[s[start]]-=1
    start+=1
    end+=1
    comp[s[end-1]]+=1
    for key in standard:
        if standard[key]!=comp[key]:
            flag=0
            break
    if flag==1:
        answer+=1
print(answer)