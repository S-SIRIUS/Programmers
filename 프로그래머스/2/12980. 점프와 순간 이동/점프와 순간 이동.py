def solution(n):
    answer=0
    while True:
        if n==0:
            break
        if n%2==0:
            n=n//2
        else:
            n-=1
            answer+=1
    
    return answer