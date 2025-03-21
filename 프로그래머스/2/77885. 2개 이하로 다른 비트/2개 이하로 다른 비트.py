   
def change(data):
    result=0
    if data %2 ==0:
        result = data+1
    else:
        data = list(bin(data)[2::])
        index=0
        if '0' not in data:
            data = ['0']+data
            data[0] = '1'
            index=0
        else:
            for i in range(len(data)-1, -1, -1):
                if data[i]=='0':
                    index=i
                    break
        data[index]='1'
        for i in range(index+1, len(data)):
            if data[i]=='1':
                index2=i
                break
        data[index2]='0'
        result = "".join(data)
        result = int(result,2) 
    return result
def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(change(n))
    return answer