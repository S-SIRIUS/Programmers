# 회의실 배정하기(골드5)
n = int(input())
array=[]
for i in range(n):
    a, b = map(int, input().split())
    array.append((a,b))
array.sort(key=lambda x: (x[1], x[0]))

standard = array[0][1]
answer=1
for i in range(1, len(array)):
    if array[i][0] >= standard:
        answer+=1
        standard = array[i][1]
print(answer)