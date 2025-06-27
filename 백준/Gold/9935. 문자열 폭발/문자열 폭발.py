# 문자열 폭발
a = list(input().strip())
b = list(input().strip())
length = len(b)
stack=[]
for i in a:
    stack.append(i)
    if stack[len(stack)-length:len(stack)] == b:
        for i in range(length):
            stack.pop()
if stack:
    print(*stack, sep="")
else:
    print("FRULA")