def solution(arr1, arr2):
    answer=[]
    len_p = len(arr1[0])
    len_arr2 = len(arr2[0])
    
    for arr_p in arr1:
        arr=[]
        for j in range(len_arr2):
            summ=0
            for k in range(len_p):
                summ += arr_p[k] * arr2[k][j]
            arr.append(summ)
        answer.append(arr)
    return answer