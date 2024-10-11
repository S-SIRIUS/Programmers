# 문자열 뒤집기(실버5)
s = list(input())
zero=0
one=0
before=''
for i in s:
    if before==i:
        continue

    if i=="0":
        zero+=1
    else:
        one+=1
    before=i
if one < zero:
    print(one)
else:
    print(zero)