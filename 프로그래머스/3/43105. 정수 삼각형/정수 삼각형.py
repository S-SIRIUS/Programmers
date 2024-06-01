def solution(triangle):
    
    for i in range(1, len(triangle)):
        # 이전값 (n개)
        before = triangle[i-1]
    
        for j in range (0, len(triangle[i])):
            # 끝자리들은 그냥가고 중간에 있는것들은 둘중에 큰거 선택해서 넣기
            if j==0: 
                triangle[i][j] += before[0]
            elif (j == len(triangle[i])-1):
                triangle[i][j] += before[-1]
            else:
                if before[j-1] > before[j]:
                    triangle[i][j] += before[j-1]
                else:
                    triangle[i][j] += before[j]
            
    return max(triangle[i])