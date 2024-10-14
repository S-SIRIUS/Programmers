def binary_check(a, b):
    if bin(a).replace("0b", "").count("1") == bin(b).replace("0b","").count("1"):
        return True
    else:
        return False
def solution(n):
    target = n
    while target<=1000000:
        target+=1
        if binary_check(n, target):
            break
    
    return target