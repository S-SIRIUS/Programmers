def solution(participant, completion):
    
    participant_dic={}
    for p in participant:
        if p in participant_dic:
            participant_dic[p]+=1
        else:
            participant_dic[p]=1
    
    for c in completion:
        if c in participant_dic:  
            participant_dic[c]-=1
    
    for ans in participant_dic:
        if participant_dic[ans]==1:
            return ans
            