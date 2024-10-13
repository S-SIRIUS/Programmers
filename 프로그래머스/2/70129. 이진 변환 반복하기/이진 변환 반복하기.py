def change_binary(s):
    
    target = len(s)
    return (bin(target).replace("0b",""))
    
    
def check_zero(s):
    count=0
    for i in s:
        if i== "0":
            count+=1
    return count

def solution(s):
    count=0
    change=0
    while True:
        if s=="1":
            break
        count+=check_zero(s)
        s=s.replace("0","")
        s=change_binary(s)
        change+=1
    answer=[change, count]
    return answer