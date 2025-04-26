# 사이클 단어(실버4)
def check(a, b):
    new_a = a+a
    if b in new_a:
        return True
    else:
        return False
n = int(input())
data = []
for i in range(n):
    data.append([input(),0])
answer=0
for i in range(n):
    if data[i][1]==1:
        continue
    else:
        compare = data[i][0]
        answer+=1
        for j in range(i+1, n):
            compare2 = data[j][0]
            if len(compare)==len(compare2):
                if check(compare, compare2):
                    data[j][1]=1
print(answer)