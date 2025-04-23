from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        candidates=[]
        dic = {}
        for o in orders:
            temp = list(o)
            temp.sort()
            candidates = list(combinations(temp,c))
            for cs in candidates:
                target=""
                for s in cs:
                    target+=s
                if target in dic:
                    dic[target]+=1
                else:
                    dic[target]=1
        if len(dic)!=0:
            maxi = max(dic.values())
            for key in dic:
                if dic[key]==maxi and dic[key]>=2:
                    answer.append(key)
    answer.sort()
    return answer