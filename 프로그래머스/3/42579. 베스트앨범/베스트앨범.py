def solution(genres, plays):
    answer = []
    play_dic={}
    index_dic={}
    index=0
    for i, j in zip(genres, plays):
        if i in play_dic:
            play_dic[i]+=j
            index_dic[i][index]=j
            
        else:
            play_dic[i]=j
            index_dic[i]={index:j}
        index+=1
        
    
    new_genres=[]
    
    target_keys = list(play_dic.keys())
    sorted_dict = sorted(play_dic.items(), key=lambda item: (-item[1]))
    sorted_dict = dict(sorted_dict)
    
    new_index_dic={}
    for i in sorted_dict.keys():
        target = index_dic[i]
        target_keys = list(target.keys())
        sorted_dict = sorted(target.items(), key=lambda item: (-item[1], target_keys.index(item[0])))
        sorted_dict = dict(sorted_dict)
        new_index_dic[i]=sorted_dict
    
    for i in new_index_dic.keys():
        target = new_index_dic[i]
        
        standard=0
        for j in target.keys():
            answer.append(j)
            standard+=1
            if(standard==2):
                break
    return answer