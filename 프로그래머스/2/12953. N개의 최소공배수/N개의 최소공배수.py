def solution(arr):
    answer = 0
    max_val = max(arr)
    num=2
    while True:
        maxi=max_val*num
        
        count=0
        for i in arr:
            if maxi % i !=0:
                break
            else:
                count+=1
        if count==len(arr):
            answer=maxi
            break
        num+=1
        
    
    return answer