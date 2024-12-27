# 블루레이 만들기
n, m = map(int, input().split())
lesson = list(map(int, input().split()))
start = max(lesson)
end = sum(lesson)
while start <= end:
    middle = (start + end)//2
    sum_size=0
    count=0
    for i in range(0, n):
        if sum_size + lesson[i] > middle:
           count+=1
           sum_size=0
        sum_size+=lesson[i]
    if sum_size!=0:
        count+=1
    if count > m:
        start = middle+1
    else:
        end = middle-1
print(start)