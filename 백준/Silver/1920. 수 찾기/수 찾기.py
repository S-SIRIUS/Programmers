# 수 찾기(실버4)
data_n = int(input())
data=list(map(int, input().split()))
data.sort()
find_n = int(input())
find_data = list(map(int, input().split()))
for i in find_data:
    start=0
    end=len(data)-1
    flag=False
    while start <= end:
        middle = (start+end)//2
        if data[middle]==i:
            flag=True
            break
        elif data[middle]>i:
            end = middle-1
        else:
            start = middle+1
    if flag:
        print(1)
    else:
        print(0)