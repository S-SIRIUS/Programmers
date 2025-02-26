from itertools import combinations
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def solution(weights):
    answer = 0
    candidates = combinations(weights, 2)
    for c in candidates:
        print(c)
        g = gcd(c[0], c[1])
        a1 = c[0]//g
        a2 = c[1]//g

        if a1 in (1, 2, 3, 4) and a2 in (1,2,3,4):
            answer+=1
    return answer