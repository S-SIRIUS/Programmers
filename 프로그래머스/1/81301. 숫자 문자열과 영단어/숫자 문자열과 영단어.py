def solution(s):
    lib = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
           'six':6, 'seven':7, 'eight':8, 'nine':9}
    string=''
    result=''
    for i in s:
        if string in lib:
            result+=str(lib[string])
            string=''
        if ord('0')<=ord(i)<=ord('9'):
            result+=i
            continue
        else:
            string+=i
    if string !='':
        if string in lib:
            result+=str(lib[string])
    return int(result)