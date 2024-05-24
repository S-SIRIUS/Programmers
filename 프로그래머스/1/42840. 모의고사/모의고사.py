def solution(answers):
    answer = []
    
    n1=[1, 2, 3, 4, 5]
    n2=[2, 1, 2, 3, 2, 4, 2, 5]
    n3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ln1= len(n1)
    ln2 = len(n2)
    ln3 = len(n3)
    
    n1_index=0
    n2_index=0
    n3_index=0
    
    n1_score=0
    n2_score=0
    n3_score=0
    
    for a in answers:    
        if a == n1[n1_index]:
            n1_score+=1
        if a == n2[n2_index]:
            n2_score+=1
        if a == n3[n3_index]:
            n3_score+=1
        n1_index+=1
        n2_index+=1
        n3_index+=1
        if(n1_index == ln1):
            n1_index=0
        if(n2_index == ln2):
            n2_index=0
        if(n3_index == ln3):
            n3_index=0
        
    ans = [n1_score, n2_score, n3_score]
    
    ans = max(ans)
    
    if(n1_score == ans):
        answer.append(1)
    
    if(n2_score == ans):
        answer.append(2)
    
    if(n3_score == ans):
        answer.append(3)
    
    print(n1_score, n2_score, n3_score)
    
    return answer