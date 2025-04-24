def solution(gems):
    answer = []
    length = len(set(gems))
    dic = dict()
    start=0
    end=0
    dic[gems[start]]=1
    flag=0
    while end < len(gems)-1:
        if len(dic)==length:
            flag=1
        if flag==1:
            if dic[gems[start]]==1:
                answer.append((start+1, end+1, end-start))
                del dic[gems[start]]
                flag=0
            else:
                dic[gems[start]]-=1
            start+=1
        else:
            end+=1
            if gems[end] in dic:
                dic[gems[end]]+=1
            else:
                dic[gems[end]]=1
    r_answer=[]
    if len(dic)==length:
        while True:
            if dic[gems[start]]==1:
                answer.append((start+1, end+1, end-start))
                del dic[gems[start]]
                flag=0
                break
            else:
                dic[gems[start]]-=1
            start+=1
    answer.sort(key=lambda x:(x[2], x[0]))
    r_answer=[answer[0][0], answer[0][1]]
    return r_answer