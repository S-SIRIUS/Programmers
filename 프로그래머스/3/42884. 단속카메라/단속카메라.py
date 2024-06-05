def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[0] and x[1])
    
    start = routes[0][1]
    print (routes)
    for route in routes:
        if route[0] > start:
            start = route[1]
            answer+=1
            
    return answer+1