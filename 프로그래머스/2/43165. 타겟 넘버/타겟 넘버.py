answer=0

def solution(numbers, target, count=1, summ=0):  
    global answer
    
    if count > len(numbers):
        if summ==target:
            answer+=1
        return
    
    else:
        before=summ
        summ+=numbers[count-1]
        solution(numbers, target, count+1, summ)
        
        before-=numbers[count-1]
        solution(numbers, target, count+1, before)
    
    return answer