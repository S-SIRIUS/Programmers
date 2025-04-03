# 단축키 지정(실버1)
n = int(input())
check=set()
for i in range(n):
    flag=0
    original_string = input()
    strings = original_string.split(" ")
    for i in range(len(strings)):
        if strings[i][0].upper() not in check:
            check.add(strings[i][0].upper())
            flag=1
            strings[i]= "[" + strings[i][0] + "]" + strings[i][1:]
            break
    
    if flag==1:
        print(" ".join(strings))
    else:
        an_flag=0
        for i in range(len(original_string)):
            if original_string[i].upper() not in check and original_string[i]!=" ":
                check.add(original_string[i].upper())
                print(original_string[0:i] + "["+original_string[i]+"]"+original_string[i+1:])
                an_flag=1
                break
        if an_flag==0:
            print(original_string)
