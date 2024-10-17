
def check(s):
    
    stack=[]
    for i in s:
        if stack and (stack[-1] == "[" and i=="]"):
            stack.pop()
        elif stack and (stack[-1] == "(" and i==")"):
            stack.pop()
        elif stack and (stack[-1] == "{" and i=="}"):
            stack.pop()
        else:
            stack.append(i)
            
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0 
    for _ in range(len(s)):
        if check(s):
            answer+=1
        s = s[1:] + s[0]
    return answer