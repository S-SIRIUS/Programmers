import math
def change_time(time):
    temp_time = time.split(":")
    return (int(temp_time[0])*60 + int(temp_time[1]))
    
def cal_payments(records_dict, fees):
    result=[]
    for key in records_dict:
        length = len(records_dict[key][0])
        total_time=0
        for i in range(0, length):
            total_time += change_time(records_dict[key][1][i]) - change_time(records_dict[key][0][i])
        if total_time <= fees[0]:
            result.append(fees[1])
        else:
            result.append(fees[1] + ((math.ceil((total_time-fees[0])/fees[2])) * fees[3]))
    return result
            
def solution(fees, records):
    answer = []
    records_dict={}
    
    for r in records:
        temp = r.split(" ")
        if temp[1] not in records_dict:
            records_dict[temp[1]]=[[], []]
        if temp[2]=="IN":
            records_dict[temp[1]][0].append(temp[0])
        else:
            records_dict[temp[1]][1].append(temp[0])
    
    records_dict = dict(sorted(records_dict.items())) # 정렬
    
    for key in records_dict:
        if len(records_dict[key][0]) > len(records_dict[key][1]):
            records_dict[key][1].append('23:59')
    answer = cal_payments(records_dict, fees)
    return answer