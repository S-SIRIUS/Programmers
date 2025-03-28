from functools import reduce
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def solution(arrayA, arrayB):
    answer = 0
    
    max_a = reduce(gcd, arrayA)
    
    max_b = reduce(gcd, arrayB)
    
    a_flag=1
    if max_a!=1:
        for b in arrayB:
            if b%max_a==0:
                a_flag=0
                break
    else:
        a_flag=0
    
    b_flag=1
    if max_b!=1:
        for a in arrayA:
            if a%max_b==0:
                b_flag=0
                break
    else:
        b_flag=0
    
    if a_flag==1 and b_flag==1:
        answer = max(max_a, max_b)
    elif a_flag==1:
        answer = max_a
    elif b_flag==1:
        answer = max_b
    else:
        answer =0
    return answer