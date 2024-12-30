# 배열에서 K번째 수 찾기(골드2)
n = int(input())
m = int(input())
start = 1
end = m
while start <= end:
    middle = (start+end)//2

    total=0
    for i in range(1, n+1):
        total+=min(n, middle//i)
    if total > m-1:
        end = middle-1
    else:
        start= middle+1
print(start)