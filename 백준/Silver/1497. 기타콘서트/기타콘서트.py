# 기타콘서트(실버1)
from itertools import combinations
import sys
input = sys.stdin.readline
def change(data):
    list_d=[]
    for i in range(0, len(data)):
        if data[i] =='Y':
            list_d.append(i+1)
    return list_d

def check(data):
    standard = set()
    for d in data:
        for j in dic[d]:
            standard.add(j)
    
    return len(standard)

n, m = map(int, input().split())
dic = {}
list_company=[]
for i in range(n):
    company, yn = map(str, input().split())
    list_company.append(company)
    dic[company] = change(yn)

maxi=-999
answer=0
for i in range(1, n+1):
    c_c = combinations(list_company, i)
    for c in c_c:
        if maxi < check(c):
            maxi = check(c)
            answer=i
if maxi==0:
    print(-1)
else:
    print(answer)