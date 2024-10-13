
def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    summ=0
    for i in range(0, len(A)):
        summ+=(A[i]*B[i])
        
    return summ