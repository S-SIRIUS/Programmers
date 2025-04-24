# 펠린드롬 만들기(실버2)
import copy
def check(string):
    start=0
    end=len(string)-1
    flag=0
    while start<=end:
        if string[start]== string[end]:
            start+=1
            end-=1
        else:
            flag=1
            break
    if flag==1:
        return False
    else:
        return True
string = input()
answer = []
for i in range(len(string)):
    target = string[i:]
    if check(target):
        break
    else:
        answer.append(string[i])
while answer:
    string+=answer.pop()
print(len(string))