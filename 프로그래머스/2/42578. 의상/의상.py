def solution(clothes):
    clothes_dic={}
    
    for i in clothes:
        if i[1] in clothes_dic:
            clothes_dic[i[1]]+=1
        else:
            clothes_dic[i[1]]=1
    ans=len(clothes)
    
    if(len(clothes_dic)>1):
        ans=0
        base=1
        for i in clothes_dic:
            base *= (clothes_dic[i]+1)
        ans+=base
        ans-=1
    return ans