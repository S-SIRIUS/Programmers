import itertools
def solution(k, dungeons):
    answer = 0

    p_order = list(itertools.permutations(dungeons))
    

    a_list=[]
    for p in p_order:
        current_k=k
        answer=0
        for i in p:
            minpilodo, consumepilodo = i
            
            if current_k >= minpilodo:
                current_k -= consumepilodo
                answer+=1
        a_list.append(answer)
    return max(a_list)