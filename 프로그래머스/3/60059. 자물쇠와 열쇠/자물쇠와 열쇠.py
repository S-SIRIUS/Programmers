def spin(key):
    return [list(row) for row in zip(*key[::-1])]

def check(key, lock, x_offset, y_offset):
    len_lock = len(lock)
    len_key = len(key)
    
    for i in range(len_lock):
        for j in range(len_lock):
            key_x, key_y = i - x_offset, j - y_offset
            if 0 <= key_x < len_key and 0 <= key_y < len_key:
                if lock[i][j] + key[key_x][key_y] != 1:
                    return False
            elif lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    len_lock, len_key = len(lock), len(key)

    for _ in range(4):  # 4번 회전
        key = spin(key)
        for x_offset in range(-len_key + 1, len_lock):
            for y_offset in range(-len_key + 1, len_lock):
                if check(key, lock, x_offset, y_offset):
                    return True
    return False