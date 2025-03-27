def solution(n):
    answer = []
    candidates=[[0]*(n+1) for _ in range(n+1)]
    state=0
    dx=[1, 0, -1]
    dy=[0, 1, 0]
    x, y = 1, 1;
    data=1
    start_index=1
    for i in range(n, 0, -1):
        if state==0:
            for j in range(i):
                candidates[x][y]=data
                x += dx[state]
                y += dy[state]
                data+=1
            x-=dx[state]
            data-=1
            state=1
        elif state==1:
            candidates[x][y]=data
            for j in range(i):
                x += dx[state]
                y += dy[state]
                data+=1
                candidates[x][y]=data
            state=2
        else:
            for j in range(i):
                x += dx[state]
                y += dy[state]
                data+=1
                candidates[x][y] = data
            start_index+=1
            x+=1
            y=start_index
            state=0
            data+=1
    for cs in candidates:
        for c in cs:
            if c!=0:
                answer.append(c)
    return answer