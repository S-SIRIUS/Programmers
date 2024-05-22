from itertools import permutations
def solution(numbers):
    
    numbers2=list(map(str,numbers))
    numbers2.sort(key = lambda x: x*3, reverse=True)
    ans=""
    for p in numbers2:
        ans+=str(int(p))
    return str(int(ans))