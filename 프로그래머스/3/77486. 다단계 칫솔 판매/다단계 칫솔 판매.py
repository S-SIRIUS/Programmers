
def dfs(key_matching, enroll, referral, name, now_amount, result):
    index = key_matching[name]
    if int(now_amount*0.1)<1:
        result[index]+=int(now_amount)
        return result
    else:
        result[index]+=int(now_amount)-int(now_amount*0.1)
    
    if referral[index]=="-":
        return result
    else:
        return dfs(key_matching, enroll, referral, referral[index], int(now_amount*0.1), result)
    

def solution(enroll, referral, seller, amount):
    answer = []
    key_matching={}
    for i in range(0, len(enroll)):
        key_matching[enroll[i]]=i
    result=[0]*(len(enroll))
         
    for i in range(0, len(seller)):
        now_amount = amount[i]*100
        result = dfs(key_matching, enroll, referral, seller[i], now_amount, result)
    
    return result