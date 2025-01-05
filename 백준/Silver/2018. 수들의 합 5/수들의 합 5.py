# 수들의 합(실버5)
n = int(input())
start=1
end=1
answer=0
total=1
while end <= n:
    if total < n:
        end+=1
        total+=end
    elif total==n:
       answer+=1
       end+=1
       total+=end
    else:
        total-=start
        start+=1
print(answer)