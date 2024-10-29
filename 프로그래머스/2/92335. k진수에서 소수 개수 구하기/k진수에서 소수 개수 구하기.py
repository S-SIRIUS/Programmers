import math
def convert(value, n):
    arr=["0","1","2","3",'4','5','6','7','8','9','A','B','C','D','E','F']
    q, r = divmod(value, n)
    
    if q==0:
        return arr[r]
    else:
        return convert(q,n) + arr[r]

def isPrime(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True
def checkPrime(str_n):
    new_ns = str_n.split("0")
    answer=0
    print(new_ns)
    for new_n in new_ns:
        if new_n !='':
            if isPrime(int(new_n)):
                print(new_n)
                answer+=1
    return answer
def solution(n, k):
    answer = -1
    converted = convert(n, k)
    answer = checkPrime(converted)
    return answer