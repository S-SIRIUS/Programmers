visited = dict()
def insert(data):
    if data in visited:
        visited[data]+=1
    else:
        visited[data]=1

def cal():
    answer=0
    for key in visited:
        if visited[key]>=2:
            answer+=1
    return answer

def point(start, target, t):
    s_x, s_y = start
    t_x, t_y = target
    answer = 0
    time=t
    if time==0:
        insert(str(time)+str(":")+str(s_x)+str(":")+str(s_y))
    if s_x == t_x and s_y == t_y:
        return time
    else:
        if s_x < t_x:
            while s_x < t_x:
                time+=1
                s_x+=1
                insert(str(time)+str(":")+str(s_x)+str(":")+str(s_y))
        elif s_x > t_x:
            while s_x > t_x:
                time+=1
                s_x-=1
                insert(str(time)+str(":")+str(s_x)+str(":")+str(s_y))
        if s_y < t_y:
            while s_y < t_y:
                time+=1
                s_y+=1
                insert(str(time)+str(":")+str(s_x)+str(":")+str(s_y))
        elif s_y > t_y:
            while s_y > t_y:
                time+=1
                s_y-=1
                insert(str(time)+str(":")+str(s_x)+str(":")+str(s_y))
        return time

def solution(points, routes):
    answer = 0
    dic = dict()
    for i in range(1, len(points)+1):
        dic[i]=points[i-1]
    for i in range(len(routes)):
        main_time=0
        for j in range(0, len(routes[i])-1):
            main_time = point(dic[routes[i][j]], dic[routes[i][j+1]], main_time)
    answer = cal()
    return answer