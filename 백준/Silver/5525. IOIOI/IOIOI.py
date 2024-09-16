#IOIOI(실버1)
def check(n, m, s):

    i=0
    count=0
    answer=0
    while i < m:
        if s[i:i+3] == "IOI":
            count+=1
            if count == n:
                answer+=1
                count-=1
            i+=2
        else:
            count=0
            i+=1
    return answer

n = int(input())
m = int(input())
s = input()
print(check(n,m,s))