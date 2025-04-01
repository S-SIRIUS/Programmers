from collections import Counter
def solution(N, stages):
    result = []
    result_list=[0]*(N+2)
    r_list=[]
    c = Counter(stages)
    for cs in c:
        result_list[cs]=c[cs]
    
    for r in range(N, 0, -1):
        result_list[r] += result_list[r+1]
    
    for i in range(1, N+1):
        if i not in c:
            r_list.append((0, i))
        else:
            r_list.append((float(c[i])/float(result_list[i]), i))
    r_list.sort(key = lambda x:(-x[0], x[1]))
    for r in r_list:
        result.append(r[1])
    return result