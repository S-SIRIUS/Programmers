dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(dirs):
    answer = 0
    visited=[]
    direction=-1
    x=0
    y=0
    
    for d in dirs:
        if d == "U":
            direction=0
        elif d =="D":
            direction=1
        elif d=="L":
            direction=2
        elif d=="R":
            direction=3
        
        new_x =  x + dx[direction]
        new_y =  y + dy[direction]
        
        if new_x < -5 or new_x > 5 or new_y >5 or new_y <-5:
            continue
        
        if [(x, y),(new_x, new_y)] in visited or [(new_x, new_y), (x, y)] in visited:
            x = new_x
            y = new_y
        
        else:
            visited.append([(x,y), (new_x, new_y)])
            answer+=1
            x = new_x
            y = new_y
    return answer