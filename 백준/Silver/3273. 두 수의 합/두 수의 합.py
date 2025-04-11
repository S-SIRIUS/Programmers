# 두수의 합(실버3)
n=int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())
start=0
end=n-1
answer=0
total=data[start]+data[end]
while end <= n-1 and start < end:
    if total ==x:
        answer+=1
        total-=data[end]
        end-=1
        total+=data[end]
        total-=data[start]
        start+=1
        total+=data[start]
    elif total > x:
        total-=data[end]
        end-=1
        total+=data[end]
    else:
        total-=data[start]
        start+=1
        total+=data[start]
print(answer)