def back(numbers):
    result=[-1]*(len(numbers))
    
    stack=[]
    for i in range(len(numbers)-1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(numbers[i])
            
    return result

def solution(numbers):
    answer = back(numbers)
    return answer