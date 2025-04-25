def diff_minute(start, end):
    hour_1, minute_1 = start.split(":")
    hour_2, minute_2 = end.split(":")
    total=0
    total += (int(hour_2)-int(hour_1))*60 
    total += (int(minute_2) - int(minute_1))
    return total

def make_string(original, minute):
    music_length = len(original)
    new_music=""
    index=0
    counts=0
    if music_length < minute: # 늘리기
        while True:
            if counts==minute:
                break
            new_music+=original[index]
            if index+1==music_length:
                index=0
            else:
                index+=1
            counts+=1
    else: # 컷팅
        new_music += original[:minute]
    return new_music

def replace_sharp(string):
    string = string.replace("C#", 'c')
    string = string.replace("D#", 'd')
    string = string.replace("F#", 'f')
    string = string.replace("G#", 'g')
    string = string.replace("A#", 'a')
    string = string.replace("B#", 'b')
    return string
def checker(new_string, target):
    if target in new_string:
        return True
    else:
        return False
def solution(m, musicinfos):
    candidates = []
    order=0
    for mi in musicinfos:
        new_music_infos = mi.split(",")
        total = diff_minute(new_music_infos[0], new_music_infos[1])
        new_music = replace_sharp(new_music_infos[3])
        new_string = make_string(new_music,total)
        new_m = replace_sharp(m)
        if checker(new_string, new_m):
            candidates.append((total, order, new_music_infos[2]))
        order+=1
    answer=""
    if len(candidates)==0:
        answer = "(None)"
    else:
        candidates.sort(key = lambda x:(-x[0], x[1]))
        answer = candidates[0][2]
    return answer