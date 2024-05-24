def solution(sizes):
    answer = 0
    
    maxi=0
    mini=0
    for i in sizes:
        if(i[0] > i[1]):
            if(i[0] > maxi):
                maxi = i[0]
            if(i[1] > mini):
                mini = i[1]
        else:
            if(i[1] > maxi):
                maxi = i[1]
            if(i[0] > mini):
                mini = i[0]
                
    answer = mini*maxi
    return answer