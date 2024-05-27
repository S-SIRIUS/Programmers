def solution(citations):
    citations.sort(reverse=True)
    answer=0
    for i in range(0, len(citations)):
        if citations[i] > answer:
            answer+=1
        else:
            break
    return answer