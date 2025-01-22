# 최대공약수(실버1)
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
answer = gcd(b,a)
print(str(1)*answer)