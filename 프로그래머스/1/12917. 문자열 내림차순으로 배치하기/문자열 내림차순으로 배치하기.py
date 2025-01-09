def solution(s):
    str_list = list(s)
    str_list.sort(reverse=True)
    answer = ''.join(str_list)
    return answer