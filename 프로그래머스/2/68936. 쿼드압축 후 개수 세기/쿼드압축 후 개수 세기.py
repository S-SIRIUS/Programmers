zero=0
one=0

def zipped(x, y, n, arr):
    global zero
    global one
    flag=0
    if n==1:
        if arr[x][y]==1:
            one+=1
        else:
            zero+=1
        return
    
    standard=arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j]!=standard:
                flag=1
                break
    if flag==1:
        zipped(x, y, n//2, arr)
        zipped(x, y+n//2, n//2, arr)
        zipped(x+n//2, y, n//2, arr)
        zipped(x+n//2, y+n//2, n//2, arr)
    else:
        if standard==1:
            one+=1
        else:
            zero+=1
    return

def solution(arr):
    answer = []
    n = len(arr)
    zipped(0, 0, n, arr)
    answer.append(zero)
    answer.append(one)
    return answer