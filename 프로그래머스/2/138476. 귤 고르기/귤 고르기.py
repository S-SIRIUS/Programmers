from collections import Counter
def solution(k, tangerine):
    t_count = Counter(tangerine)
    sorted_counts = sorted(t_count.values(), reverse=True)
    
    total = 0
    kinds = 0  

    for count in sorted_counts:
        total += count
        kinds += 1
        if total >= k:
            break

    return kinds

'''
def solution(k, tangerine):
    n = len(tangerine)
    t_dict={}
    
    kinds = set(tangerine)
    
    for kind in kinds:
        t_dict[kind]=0
    
    for t in tangerine:
        t_dict[t]+=1
    
    while n>k:
        key = min(t_dict, key=t_dict.get)
        t_dict[key]-=1
        if t_dict[key]==0:
            del(t_dict[key])
        n-=1
    return len(t_dict)
'''