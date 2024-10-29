def LZW(msg, dictionary, index):
    answer = []
    start=1
    candi=0
    while msg and start <= len(msg):
        if msg[0:start] in dictionary:
            candi = dictionary[msg[0:start]]
            start+=1
        else:
            dictionary[msg[0:start]] = index                   
            index+=1
            msg=msg[start-1:]
            answer.append(candi)
            start=1
    if candi!=0:
        answer.append(candi)
    return answer

def solution(msg):
    answer = []
    dictionary = {}
    index=1
    for i in range(ord('A'), ord('Z')+1):
        dictionary[chr(i)] = index
        index+=1
    answer = LZW(msg, dictionary, 27)
    
    return answer