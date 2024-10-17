from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    for i in range (0, len(discount)-9):
        count=0
        ten_list = discount[i:i+10]
        ten_dict = Counter(ten_list)
        for i in range(0, len(number)):
            if number[i] == ten_dict[want[i]]:
                count+=1
        if count==len(number):
            answer+=1
    return answer