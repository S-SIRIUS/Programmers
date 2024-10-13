def solution(s):
    answer = ''    
    string_list = s.split(" ")
    new_word_list=[]
    for string in string_list:
        word_list = list(string)
        for i in range(0, len(word_list)):
            if i == 0:
                if ord('a') <=ord(word_list[i]) <=ord('z'):
                    word_list[i] = chr(ord(word_list[i])-32)
                else:
                    continue
            else:
                if ord('A') <= ord(word_list[i]) <= ord('Z'):
                    word_list[i] = chr(ord(word_list[i])+32)
        
        new_word_list.append("".join(word_list))
    
    answer = " ".join(new_word_list)
    return answer