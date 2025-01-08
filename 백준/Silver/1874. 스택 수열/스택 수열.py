# 스택수열(실버2)
import sys
input = sys.stdin.readline

n = int(input())
answer=[]
for i in range(n):
    answer.append(int(input()))

stack=[]
answer_index=0
print_value=[]
for number in range (1, n+1):
    stack.append(number)
    print_value.append('+')
    while stack:
        if stack[-1] == answer[answer_index]:
            answer_index+=1
            stack.pop()
            print_value.append('-')
        else:
            break
if len(stack)>0:
    print("NO")
else:
    for i in print_value:
        print(i)