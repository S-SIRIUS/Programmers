# 문자열(실버4)
def compare(a, b):
    answer=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            answer+=1
    return answer

a, b = map(str, input().split())
candidates=[]
for i in range(len(b)):
    if i+len(a)<=len(b):
        candidates.append(compare(a, b[i:i+len(a)]))
print(min(candidates))