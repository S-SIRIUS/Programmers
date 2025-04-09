# 문자열 잘라내기
from collections import defaultdict
strings = []
r, c = map(int, input().split())
for i in range(r):
    strings.append(list(input()))

start=0
end=r-1
answer=0
while start <= end:
    middle = (start+end)//2
    s_dict = defaultdict(int)
    flag=1
    for j in range(c):
        temp=""
        for i in range(middle, r):
            temp+=strings[i][j]
        # 중복이 없음
        if s_dict[temp]==0:
            s_dict[temp]+=1
        else: # 중복이 있음(break)
            flag=0
            break
    # 중복이 없으면(범위 줄여본다)
    if flag==1:
        answer=middle
        start=middle+1
    else: # 중복이 있으면(범위 늘려본다)
        end = middle-1
print(answer)