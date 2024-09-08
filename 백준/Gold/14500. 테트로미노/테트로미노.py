def dfs(x, y, depth, total):
    global max_sum
    if depth == 4:  # 4개의 칸을 채운 경우
        max_sum = max(max_sum, total)
        return

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + field[nx][ny])
            visited[nx][ny] = False

def check_special_shape(x, y):
    global max_sum
    for i in range(4):
        total = field[x][y]
        for j in range(3):
            k = (i + j) % 4
            nx, ny = x + directions[k][0], y + directions[k][1]
            if 0 <= nx < n and 0 <= ny < m:
                total += field[nx][ny]
            else:
                break
        max_sum = max(max_sum, total)

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정 (우, 하, 좌, 상)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

max_sum = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # DFS를 이용하여 ㅗ 모양 제외한 모든 모양 탐색
        visited[i][j] = True
        dfs(i, j, 1, field[i][j])
        visited[i][j] = False

        # ㅗ 모양 탐색
        check_special_shape(i, j)

print(max_sum)
