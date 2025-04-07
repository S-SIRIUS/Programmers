def make_index(data):
    if data=="code":
        standard=0
    elif data=="date":
        standard=1
    elif data=="maximum":
        standard=2
    else:
        standard=3
    return standard

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    standard=0
    
    standard = make_index(ext)
    candidates=[]
    for d in data:
        if d[standard] < val_ext:
            candidates.append(d)
    standard2 = make_index(sort_by)
    candidates.sort(key=lambda x: x[standard2])
    return candidates