import math
def solution(n, stations, w):
    answer = 0
    arrange_list=[]
    start=1
    for s in stations:
        arrange_list.append((start, s-w-1))
        start=s+w+1
    if start <= n:
        arrange_list.append((start, n))
    
    for i in arrange_list:
        total = i[1]-i[0]+1
        answer += math.ceil(total/(w*2+1))
    
    return answer