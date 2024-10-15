def solution(n, words):
    answer = []
    each_player={}
    player=0
    for i in range(1, n+1):
        each_player[i]=0
    data=[]
    before=words[0][0]
    for i in range (0, len(words)):
        if words[i][0]!=before or words[i] in data:
            index = (i+1)%n
            if index==0:
                index=n
            each_player[index]+=1
            player=index
            break
        else:
            index = (i+1)%n
            if index==0:
                index=n
            each_player[index]+=1    
        before = words[i][-1]
        data.append(words[i])

 
    if len(data)==len(words):
        return [0, 0]
    else:
        return [player, each_player[player]]