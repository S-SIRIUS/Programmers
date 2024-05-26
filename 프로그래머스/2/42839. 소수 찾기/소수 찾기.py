import itertools


def isPrime(num):
    count=0
    if(num==0 or num==1):
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i ==0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    made=[]
    n_made=[]
    
    for i in range(1, len(numbers)+1):
        made += list(itertools.permutations(numbers, i))
    for i in made:
        results=""
        for j in i:
            results += j
        n_made.append(int(results))
        
    for number in numbers:
        n_made.append(int(number))
        
    n_made = list(set(n_made))
    
    for target in n_made:
        if isPrime(target):
            answer+=1
            print(target)
    
    return answer