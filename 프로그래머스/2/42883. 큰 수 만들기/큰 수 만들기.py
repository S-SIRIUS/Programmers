def solution(number, k):
    
    stack=[]
    for i in number:
        
        while len(stack) >0 and k>0 and stack[-1] < i:
            stack.pop()
            k-=1
        
        stack.append(i)
    
    if k>0:
        return number[0:len(number)-k]
    else:
        return "".join(stack)