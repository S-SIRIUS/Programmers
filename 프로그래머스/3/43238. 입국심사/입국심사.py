def solution(n, times):
    answer = 0
    
    start=0
    end = min(times)*n
    
    while(start<=end):
        mid = (start+end)//2
        summ=0
        for x in times:
            summ+=mid//x
        
        if(summ >= n):
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer