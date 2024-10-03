# 곱셈(실버1)
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def divide(b):
    if b==1:
        return a % c
    
    division = divide(b//2)
    if b%2==0:
        return (division * division) % c
    else:
        return (division * division) * a %c

a, b, c = map(int, input().split())
print(divide(b))