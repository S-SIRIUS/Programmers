import sys
def multi(a,b):
    X = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                X[i][j] += a[i][k]*b[k][j] % 1000 
    return X

def square(x,size):
    if size == 1:
        return x
    v = square(x,size//2)
    if size % 2 == 0 :
        return multi(v,v)
    else : 
        return multi(multi(v,v),x)

n, b = map(int,sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = square(a,b)
for i in range(n):
    for j in range(n):
        result[i][j] = result[i][j] %1000

for k in result:
    print(*k)