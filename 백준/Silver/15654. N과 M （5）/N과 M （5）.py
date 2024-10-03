# N과 M (5) 실버3
def back(now, num, count):
    if count==m:
        print(now)
    else:
        for i in num:
            if i not in now.split():
                back(now+" "+i, num, count+1)               


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
num = list(map(str, num))
for i in num:
    back(i, num, 1)