# N과 M(2) 실버2
def back(ans, count, number):
    if count==m:
        print(ans)
        return
    else:
        for i in range(1, n+1):
            if (number < i):
                temp_ans = ans
                ans+=" " + str(i)
                back(ans, count+1, i)
                ans= temp_ans


n, m = map(int, input().split())
for i in range(1, n+1):
    back(str(i), 1, i)