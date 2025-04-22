# 로마숫자(골드5)
def change2(integer):
    answer = ""
    if integer % 1000>=0:
        value = (integer//1000)
        if value>3:
            value=3
        answer += 'M'*(value)
        integer-=value*(1000)
    if integer >=900:
        answer += 'CM'
        integer-=900
    if integer >= 500:
        value = (integer//500)
        answer+='D'*(value)
        integer-=value*(500)
    if integer >= 400:
        value = (integer//400)
        answer += 'CD'
        integer-=400
    if integer>=100:
        value = (integer//100)
        if value>3:
            value=3
        answer += 'C'*(value)
        integer-=value*(100)
    if integer >= 90:
        answer += 'XC'
        integer-=90
    if integer >= 50:
        value = (integer//50)
        answer+='L'*(value)
        integer-=value*(50)
    if integer >= 40:
        answer+='XL'
        integer-=40
    if integer >= 10:
        value = (integer//10)
        if value>3:
            value=3
        answer += 'X'*(value)
        integer-=value*(10)
    if integer >= 9:
        answer+='IX'
        integer-=9
    if integer>=5:
        value = (integer//5)
        answer+='V'*(value)
        integer-=value*(5)
    if integer >= 4:
        answer+='IV'
        integer-=4
    if integer >= 1:
        value = (integer//1)
        if value>3:
            value=3
        answer += 'I'*(value)
        integer-=value*(1)
    return answer
def change(string):
    total=0
    index=0
    while index < len(string):
        if string[index:index+2] in dic:
            total+=dic[string[index:index+2]]
            index+=2
        elif string[index:index+1] in dic:
            total+=dic[string[index:index+1]]
            index+=1
    return total

dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, 
       "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
a = input()
b = input()
summ=0
summ+=change(a)
summ+=change(b)
print(summ)
print(change2(summ))