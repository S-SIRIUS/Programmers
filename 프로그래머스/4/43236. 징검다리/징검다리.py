def solution(distance, rocks, n):
    answer = 0
    
    start=0
    rocks.sort()
    rocks.append(distance)
    end = distance
    while start <= end:
        mid = (start+end)//2
        
        delete = 0
        prev_rock=0
        for rock in rocks:
            if rock - prev_rock < mid :
                delete +=1
                
                if delete > n:
                    break
            else:
                prev_rock = rock
        if delete > n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
        
    
    return answer