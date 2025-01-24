
def recur(n, answer):
    value = n%10
    answer.append(value)
    if n<10:
        return answer
    else:
        return recur(n//10, answer )
def solution(n):
    answer = []
    answer = recur(n, answer)
    return answer