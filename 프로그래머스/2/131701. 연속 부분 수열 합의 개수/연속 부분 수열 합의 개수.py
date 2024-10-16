def solution(elements):
    answer = 0
    elements = elements * 2
    e_list=set()
    for i in range(1, len(elements)//2+1):
        for j in range(0, len(elements)):
            e_list.add(sum(elements[j:j+i]))
    return len(e_list)