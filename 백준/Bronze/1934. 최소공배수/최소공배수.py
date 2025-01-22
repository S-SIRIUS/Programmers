# 최소공배수
import sys
input = sys.stdin.readline
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(int((a*b)/gcd(a,b)))