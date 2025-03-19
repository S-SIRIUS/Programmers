from itertools import permutations
def check(user, banned):
    index=0
    flag=1
    if len(user)!=len(banned):
        flag=0
    else:
        while index < len(banned):
            if user[index]!=banned[index] and banned[index]!="*":
                flag=0
                break
            index+=1
    
    if flag==0:
        return False
    else:
        return True

def solution(user_id, banned_id):
    answer = 1
    ps = list(permutations(user_id, len(banned_id)))
    value=[]
    for p in ps:
        temp=0
        i=0
        while i < len(banned_id):
            if check(p[i], banned_id[i]):
                temp+=1
            i+=1
        if temp==len(banned_id) and set(p) not in value:
            value.append(set(p))
    return len(value)