import math
def solution(n):
    answer=-1
    value = math.sqrt(n)
    if value - int(value) == 0:
        answer= (value+1)**2
    return answer