def mk_E(text):
    return text+"님이 들어왔습니다."
def mk_L(text):
    return text+"님이 나갔습니다."

def algo(time_stamp, dic):
    result=[]
    for t in time_stamp:
        if t[1]=="Enter":
            result.append(mk_E(dic[t[0]]))
        else:
            result.append(mk_L(dic[t[0]]))
    return result
def solution(record):
    answer = []
    dic={}
    flag=0
    time_stamp=[]
    for r in record:
        new_r = r.split(" ")
        activity = new_r[0]
        id_v = new_r[1]
        if activity!="Leave":
            name = new_r[2]
        if activity!="Change":
            time_stamp.append((id_v, activity))
        if flag==id_v and activity=="Enter":
            flag=0
            dic[id_v] = name
        
        elif activity == "Leave":
            flag=id_v
        else:
            dic[id_v] = name
    answer = algo(time_stamp, dic)
    return answer