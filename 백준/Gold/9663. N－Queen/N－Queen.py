# N-Queen(골드4)
import sys
input = sys.stdin.readline
answer=0

def checkAttack(count):
    for i in range(count):
        if field[count] == field[i] or abs(field[count]-field[i])==abs(count-i):
            return True
    return False

def setQueen(count):
    global answer

    if count==n:
        answer+=1
        return
    else:
        for i in range(n):
            field[count]=i
            if checkAttack(count)==False:
                setQueen(count+1)

n = int(input())
field=[0]*(n)
setQueen(0)
print(answer)