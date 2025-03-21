import copy
from collections import deque
def check(i,j, board, new):
    standard = board[i][j]
    if standard!="*" and standard == board[i+1][j] and standard == board[i][j+1] and standard == board[i+1][j+1]:
        new[i][j]="*"
        new[i+1][j]="*"
        new[i][j+1]="*"
        new[i+1][j+1]="*"
    return new
        
def move(new, m, n):
    count=0
    for j in range(n):
        queue = deque()
        for i in range(m-1, -1, -1):
            if new[i][j]=="*":
                queue.append((i,j))
            else:
                if queue:
                    x, y = queue.popleft()
                    new[x][y]=new[i][j]
                    new[i][j]="*"
                    count+=1
                    queue.append((i,j))
    return new, count
def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    new = copy.deepcopy(board)
    while True:
        count=0
        for i in range(0, m-1):
            for j in range(0, n-1):
                new = check(i,j, board, new)
        new, count = move(new, m, n)
        board=copy.deepcopy(new)
        if count==0:
            break
    answer=0
    for b in board:
        answer+=b.count("*")
    return answer