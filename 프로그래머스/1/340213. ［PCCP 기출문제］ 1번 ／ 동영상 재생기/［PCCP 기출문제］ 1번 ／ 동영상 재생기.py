def time_compare(a, b):
    a_list = a.split(":")
    b_list = b.split(":")
    # True는 b가 a보다 큼
    if int(a_list[0]) < int(b_list[0]):
        return True
        
    elif int(a_list[0]) == int(b_list[0]):
        if int(a_list[1]) <= int(b_list[1]):
            return True
    return False
        

def op_check(time, op_start, op_end):
    if time_compare(op_start, time)==False:
        return time
    if time_compare(time, op_end)==False:
        return time
    return op_end

def time_change(minute, second):
    if second >= 60:
        minute += 1
        second = second%60
    elif second <0:
        minute -= 1
        second = 60 + second
    if second <10:
        second = "0"+str(second)
    
    if minute <0:
        minute ="00"
        second ="00"
    elif minute <10:
        minute = "0"+str(minute)
    return str(minute)+":"+str(second)

def time_cal(time, func, video_len):
    time_list = time.split(":")
    minute = int(time_list[0])
    second = int(time_list[1])
    if func=="add":
        second += 10
        time = time_change(minute, second)
        time = time_limit_check(video_len, time)
    else:
        second-=10
        time = time_change(minute, second)
    return time

def time_limit_check(video_len, time):
    if time_compare(time, video_len)==True:
            return time
    else:
        return video_len

def next_func(video_len, pos):
    pos = time_cal(pos, "add", video_len)
    return pos

def prev_func(video_len, pos):
    pos = time_cal(pos, "sub", video_len)
    return pos
    
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    pos = op_check(pos, op_start, op_end)
    for c in commands:
        if c=="next":
            pos = next_func(video_len, pos)
        else:
            pos = prev_func(video_len, pos)
        pos = op_check(pos, op_start, op_end)
    return pos