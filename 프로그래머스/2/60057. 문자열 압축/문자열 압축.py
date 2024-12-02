def solution(s):
    answers=[]
    if len(s)==1:
        return 1
    else:
        for i in range(1, len(s)//2+1):
            comparison = s[0:i]
            zi = ""
            cnt=1
            for j in range(i, len(s), i):
                now = s[j:j+i]
                if now != comparison:
                    if cnt > 1:
                        zi += str(cnt) + comparison
                    else:
                        zi += comparison
                    comparison = now
                    cnt=1
                else:
                    cnt+=1
            if cnt > 1:
                zi += str(cnt) + comparison
            else:
                zi += comparison
            answers.append(len(zi))
        return min(answers)