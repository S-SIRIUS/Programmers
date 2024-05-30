def solution(n, lost, reserve):
    answer = 0

    reserve_del = set(reserve)- set(lost)
    lost_del = set(lost) - set(reserve)
    
    print(reserve_del)
    print(lost_del)
    for i in reserve_del:
        if i-1 in lost_del: 
            lost_del.remove(i-1)
        elif i+1 in lost_del: 
            lost_del.remove(i+1)
   
    answer = n - len(lost_del)
    return answer