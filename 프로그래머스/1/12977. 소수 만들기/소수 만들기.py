from itertools import combinations
import math

def is_Prime(data):
    for i in range(2, int(math.sqrt(data))+1):
        if data % i==0:
            return False
    return True

def solution(nums):
    answer = 0
    cs = combinations(nums,3)
    for c in cs:
        if is_Prime(sum(c)):
            answer+=1

    return answer