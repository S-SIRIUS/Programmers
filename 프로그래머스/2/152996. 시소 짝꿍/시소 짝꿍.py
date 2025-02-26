from collections import Counter

def solution(weights):
    answer = 0
    c = Counter(weights)
    for w in range(100, 1001):
        if c[w]>0:
            a1 = c[w]*(c[w]-1)/2
            a2 = c[w]*(c[w*2])
            a3 = c[w]*(c[w*3/2])
            a4 = c[w]*(c[w*4/3])
            answer+=(a1+a2+a3+a4)
    return answer