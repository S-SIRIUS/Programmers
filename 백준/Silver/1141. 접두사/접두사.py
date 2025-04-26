# 접두사
n = int(input())
st_list = []
for i in range(n):
    st_list.append(input())
st_list.sort()
answer=1
for i in range(n-1):
    if st_list[i+1].startswith(st_list[i]):
        continue
    answer+=1
print(answer)