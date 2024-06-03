def solution(name):
    answer = 0
    name = list(map(str, name))
    first = ['A' for _ in range(len(name))]
    move = len(name)-1
    for left in range(0, len(name)):
        answer += min(abs(ord(name[left]) - ord(first[left])), abs(ord('Z') - ord(name[left])+1))
        
        index = left+1     
        while index < len(name) and name[index]=='A':
            index+=1
        right = len(name) - index
        distance = min(left, right)
        move = min(move, distance + left + right)
    answer += move
    return answer