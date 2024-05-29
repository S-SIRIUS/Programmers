fixed_words = ['A' ,'E', 'I', 'O', 'U']
answer=0
ranswer=0
words=""
def dfs(word, counts):
    global fixed_words
    global answer
    global r_answer
    global words
    
    if(word == words):
        r_answer= answer
    else:
        answer+=1
        if(counts > 4):
            return 
        else:
            for f_words in fixed_words:
                words += f_words
                dfs(word, counts+1)
                words = words[0:len(words)-1]
            
def solution(word):
    global r_answer
    dfs(word, 0)
    return r_answer