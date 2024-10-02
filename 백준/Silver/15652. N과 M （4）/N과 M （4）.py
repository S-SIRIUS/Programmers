# N과 M (4) 실버3
import sys
input = sys.stdin.readline

def back(now, ans, count):    
    if count==m:
        print(ans)
        return

    for i in range(1, n+1):
        if now <= i:
            temp_ans=ans
            ans += " " + str(i)
            back(i, ans, count+1)
            ans = temp_ans


n, m = map(int, input().split())

for i in range(1, n+1):
    back(i, str(i), 1)