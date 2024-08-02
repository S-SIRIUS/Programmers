all_count=0
board = []
answer = []

def check_col(board):
    global all_count
    for i in range(0, 5):
        count=0
        for j in range(0, 5):
            if board[i][j] == -999:
                count+=1
            if count==5:
                all_count+=1
                break
    return

def check_row(board):
    global all_count
    for i in range(0, 5):
        count=0
        for j in range(0, 5):
            if board[j][i] == -999:
                count+=1
            if count==5:
                all_count+=1
                break
    return

def check_diagonol(board):
    global all_count
    count=0
    for i in range(0, 5):
        if board[i][i] == -999:
            count+=1
        if count==5:
            all_count+=1
    
    count=0
    for i in range(4, -1, -1):
        if board[i][4-i] == -999:
            count+=1
        if count==5:
            all_count+=1
    return

for i in range(5):
    board.append(list(map(int ,input().split())))

for i in range(5):
    answer.append(list(map(int, input().split())))

num=0
for i in range(0, 5):
    for j in range(0, 5):
        num+=1
        for k in range(0, 5):
            if answer[i][j] in board[k]:
                board[k][board[k].index(answer[i][j])] = -999
                break # 숫자는 한개씩 있기 때문  
        
        all_count=0
        check_col(board)
        check_row(board)
        check_diagonol(board)

        if(all_count>=3):
            print(num)
            exit(0)