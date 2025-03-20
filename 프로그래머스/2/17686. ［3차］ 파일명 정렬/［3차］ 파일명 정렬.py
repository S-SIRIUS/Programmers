def lower(sts):
    new=""
    for st in sts:
        temp=st
        if ord(st) <= ord('a'):
            temp = chr(ord(st) + (ord('a') - ord('A')))
        new+=temp
    return new

def solution(files):
    answer = []
    new_array=[]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for f in range(len(files)):
        for i in range(len(files[f])):
            if files[f][i] in numbers:
                index = i
                first_index = index
                while index < len(files[f]):
                    if files[f][index] not in numbers:
                        break
                    index+=1
                HEAD=files[f][0:first_index]
                NUMBER=files[f][first_index:index]
                new_array.append((files[f], HEAD.lower(), int(NUMBER), f))
                break
    new_array.sort(key=lambda x: (x[1], x[2], x[3]))
    answer=[]
    for n in new_array:
        answer.append(n[0])
    return answer