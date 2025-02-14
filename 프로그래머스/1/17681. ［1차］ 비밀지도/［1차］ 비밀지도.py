def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        target = bin(arr1[i] | arr2[i])
        temp=''
        if len(target) - (n+2) <0:
            for i in range(n+2 - len(target)):
                temp+=' '
        for j in range(2, len(target)):
            if target[j] =='0':
                temp+=' '
            else:
                temp+='#'
        answer.append(temp)
    return answer