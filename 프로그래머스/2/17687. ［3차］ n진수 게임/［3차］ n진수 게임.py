def convert(value, n):
    arr="0123456789ABCDEF"
    q, r = divmod(value, n)
    if q==0:
        return arr[r]
    else:
        return convert(q, n) + arr[r]
    
def solution(n, t, m, p):
    answer, test = '', ''
    for i in range(m*t):
        test += str(convert(i, n))
    
    while len(answer) < t:
        answer += test[p-1]
        p+=m
    
    return answer