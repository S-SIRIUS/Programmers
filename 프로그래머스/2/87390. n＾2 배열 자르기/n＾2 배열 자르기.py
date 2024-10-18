def make_array(n, left, right):
    array=[]
    for idx in range(left, right+1):
        row = idx//n
        column = idx%n
        array.append(max(row, column)+1)
    return array
    
def solution(n, left, right):
    answer = make_array(n, left, right)
    
    return answer
