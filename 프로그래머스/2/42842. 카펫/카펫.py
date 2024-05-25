def solution(brown, yellow):
    answer = [0,0]
    
    all = brown + yellow
    
    for i in range(1, all+1):
        if(all % i ==0):
            if((i-2) * (all//i-2) == yellow):
                if(i > all//i):
                    answer[0] = i
                    answer[1] = all//i
                else:
                    answer[0] = all//i
                    answer[1] = i
                break
    return answer