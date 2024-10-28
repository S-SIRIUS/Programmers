from collections import Counter
def makeList(target):
    set_list=[]
    for i in range(0, len(target)-1):
        twice=""
        for j in range(0, 2):
            data = target[i+j].upper()
            if ord("A") <= ord(data) <=ord("Z"):
                twice += data
            else:
                twice=""
                break
        if twice!="":
            set_list.append(twice)
    return set_list

def makeAnswer(set1, set2):
    union = set(set1) | set(set2)
    intersect = set(set1) & set(set2)
    
    c_set1 = Counter(set1)
    c_set2 = Counter(set2)
    print(c_set1)
    print(c_set2)
    
    len_intersect = 0
    for i in intersect:
        if c_set1[i] < c_set2[i]:
            len_intersect+=c_set1[i]
        else:
            len_intersect+=c_set2[i]
    len_union = 0
    for i in union:
        if c_set1[i] and c_set2[i]:
            if c_set1[i] > c_set2[i]:
                len_union += c_set1[i]
            else:
                len_union += c_set2[i]
            
        elif c_set1[i]:
            len_union += c_set1[i]
        else:
            len_union += c_set2[i]
    
    
    return len_intersect, len_union

def solution(str1, str2):
    answer = 0
    str1 = makeList(str1)
    str2 = makeList(str2)
    intersect, union = makeAnswer(str1, str2)
    if intersect == union:
        answer = 65536
    else:
        answer = int(intersect/union * 65536)
    return answer