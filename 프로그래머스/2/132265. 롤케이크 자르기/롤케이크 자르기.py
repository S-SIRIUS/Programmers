from collections import Counter

def decline(key, d_p2):
    if d_p2[key]==1:
        del d_p2[key]
    else:
        d_p2[key]-=1
    return d_p2

def cut(topping):
    answer=0
    d_p1= set()
    d_p2=Counter(topping)
    
    for i in range(0, len(topping)):

        d_p1.add(topping[i])
        d_p2 = decline(topping[i], d_p2)
        
        if len(d_p1) == len(d_p2):
            answer+=1
    return answer

def solution(topping):
    answer = -1
    answer = cut(topping)
    return answer