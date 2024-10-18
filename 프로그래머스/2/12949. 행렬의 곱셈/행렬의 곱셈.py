'''
def multiply(arr1, arr2):
    answer=[]
    for arr_part in arr1:
        arr=[]
        for j in range(len(arr_part)):
            summ=0
            for k in range(len(arr2)):
                summ += arr_part[k] * arr2[k][j]
            arr.append(summ)
        answer.append(arr)
    return answer

def solution(arr1, arr2):
    answer = multiply(arr1, arr2)
    return answer


'''

def solution(arr1, arr2):
    answer = []
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])

    for i in range(m):
        arr = arr1[i]
        result = []
        for j in range(r):
            hap = 0
            for k in range(n):
                hap += arr[k] * arr2[k][j]
            result.append(hap)
        answer.append(result)

    return answer