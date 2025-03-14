def cal(level, diffs, times):
    result=0
    for i in range(len(diffs)):
        result+=times[i]
        if diffs[i] > level:
            if i>=1:
                time_prev = times[i-1]
            else:
                time_prev = 0
            result+=(diffs[i]-level)*(time_prev +times[i])
    return result

def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = 100000
    while start <= end:
        middle = (start+end)//2
        value = cal(middle, diffs, times)
        if value > limit:
            start = middle+1
        else:
            end = middle-1
            answer = middle

    return answer