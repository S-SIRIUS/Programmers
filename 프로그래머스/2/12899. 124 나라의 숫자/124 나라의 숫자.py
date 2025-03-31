def change(n):
    if n<=3:
        return str(n)
    else:
        mok = n//3
        m = n%3
        if m==0:
            mok-=1
        return str(m) + change(mok)
    

def solution(n):
    answer = ''
    answer = change(n)
    answer = answer[::-1]
    answer = answer.replace('0', '4')
    answer = answer.replace('3', '4')
    return answer