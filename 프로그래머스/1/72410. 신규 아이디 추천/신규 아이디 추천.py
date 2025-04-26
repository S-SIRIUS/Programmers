def first(string):
    return string.lower()

def second(string):
    target_list= [str(i) for i in range(0, 10)] + ['_', '.', '-']
    new_string=""
    for s in string:
        if (ord(s)>=ord('a') and ord(s)<=ord('z')) or (s in target_list): 
            new_string+=s
    return new_string
def third(string):
    while ".." in string:
        string = string.replace("..",".")
    return string
def fourth(string):
    if len(string)>=2:
        if string[0]=='.':
            string = string[1:]
        if string[-1]=='.':
            string = string[0:-1]
    else:
        if len(string)==1 and string[0]=='.':
            string=""
    return string
def fifth(string):
    if string=="":
        string = "a"
    return string
def sixth(string):
    if len(string)>=16:
        string = string[0:15]
        if string[-1]=='.':
            string = string[0:-1]
    return string
def seventh(string):
    target = string[-1]
    if len(string)<=2:
        while len(string)<=2:
            string+=target
    return string
def solution(new_id):
    answer = ''
    new_id = first(new_id)
    new_id = second(new_id)
    new_id = third(new_id)
    new_id = fourth(new_id)
    new_id = fifth(new_id)
    new_id = sixth(new_id)
    new_id = seventh(new_id)
    return new_id