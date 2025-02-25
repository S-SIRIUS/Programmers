def solution(n, results):
    answer=0
    inf = int(1e9)
    matrix = [[inf]*(n+1) for _ in range(n+1)]
    
    for r in results:
        matrix[r[1]][r[0]]=1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                matrix[i][j]=0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    for i in range(1, n+1):
        count=0
        for j in range(1, n+1):
            if matrix[i][j]!=inf or matrix[j][i]!=inf:
                count+=1
        if count==n:
            answer+=1
    return answer