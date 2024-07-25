from collections import deque
import numpy as np
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def extract_pieces(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    pieces = []
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        piece = [(x,y)]
        
        while queue:
            cx, cy = queue.popleft()
            
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == target:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    piece.append((nx, ny))
                    
        return piece
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                pieces.append(bfs(i, j))
    return pieces

def rotate(piece, n):
    min_x = min(x for x, y in piece)
    min_y = min(y for x, y in piece)
    piece = [(x-min_x, y-min_y) for x,y in piece]
    
    max_dim = max(max(x for x, y in piece), max(y for x, y in piece)) + 1
    grid = np.zeros((max_dim, max_dim), dtype=int)
    
    for x,y in piece:
        grid[x][y]=1
        
    rotations=[]
    
    for _ in range(4):
        grid = np.rot90(grid)
        new_piece = [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if grid[i][j]==1]
        min_x = min(x for x,y in new_piece)
        min_y = min(y for x,y in new_piece)
        
        new_piece = [(x-min_x, y-min_y) for x, y in new_piece]
        rotations.append(new_piece)
    return rotations

def match_piece(board, piece, x, y):
    for dx, dy in piece:
        if not (0<= x+dx < len(board) and 0<=y+dy<len(board)) or board[x+dx][y+dy]!=0:
            return False
    for dx, dy in piece:
        board[x+dx][y+dy]=1
    return True

def solution(game_board, table):
    table_pieces = extract_pieces(table, 1)
    board_spaces = extract_pieces(game_board, 0)
    used=[False] * len(table_pieces)
    filled =0
    
    for space in board_spaces:
        space_size = len(space)
        found = False
        
        for i, piece in enumerate(table_pieces):
            if used[i]:
                continue
            if len(piece) != space_size:
                continue
            
            for rotated_piece in rotate(piece, len(game_board)):
                board_copy = [row[:] for row in game_board]
                offset_x = min(x for x,y in space)
                offset_y = min(y for x,y in space)
                
                if match_piece(board_copy, rotated_piece, offset_x, offset_y):
                    filled += space_size
                    used[i] = True
                    game_board = board_copy
                    found = True
                    break
            if found:
                break
    return filled
