# 주몽의 명령(실버4)
n = int(input())
target = int(input())
ing = list(map(int, input().split()))
ing.sort()
start=0
end=n-1
total = ing[start]+ing[end]
answer=0
while start < end:

    if ing[start]+ing[end] == target:
        end-=1
        start+=1
        answer+=1
    elif ing[start]+ing[end] < target:
        start+=1
    else:
        end-=1
print(answer)