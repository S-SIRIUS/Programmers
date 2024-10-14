def solution(n):
    answer = 0
    
    num = [i for i in range(1, n+1)]
    interval_sum=0
    end=0
    answer=0
    for start in range (n):
        while interval_sum < n and end < n:
            interval_sum+=num[end]
            end+=1
        if interval_sum==n:
            answer+=1
        interval_sum-=num[start]
        
    return answer