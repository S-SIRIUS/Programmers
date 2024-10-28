def solution(s):
    new_s = s.replace("{","[").replace("}","]")
    new_s = eval(new_s)
    new_s = sorted(new_s, key=len)
    answer=[]
    for s in new_s:
        for i in s:
            if int(i) in answer:
                continue
            answer.append(int(i))
    return answer