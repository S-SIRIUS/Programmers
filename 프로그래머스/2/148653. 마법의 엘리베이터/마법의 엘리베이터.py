def check(target, list_storey, i):
    answer=0
    flag=0
    if target==0:
        answer=0
    elif 1<= target <=4:
        answer+=target
    elif target==5:
        if i-1 >= -len(list_storey) and list_storey[i-1]>=5:
            answer+=(10-target)
            flag=1
        else:
            answer+=target
    else:
        answer+=(10-target)
        flag=1
    return answer, flag

def solution(storey):
    list_storey = list(map(int, str(storey)))
    answer=0
    for i in range(-1, -len(list_storey)-1, -1):
        value, flag = check(list_storey[i], list_storey, i)
        answer+=value
        if flag==1 and i-1 >= -len(list_storey):
            list_storey[i-1]+=1
        
        elif flag==1 and i-1 < -len(list_storey):
            answer+=1
    return answer