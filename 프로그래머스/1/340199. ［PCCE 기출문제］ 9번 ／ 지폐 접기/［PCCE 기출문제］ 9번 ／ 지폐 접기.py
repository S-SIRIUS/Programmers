def rotate(bill):
    temp  = bill[0]
    bill[0] = bill[1]
    bill[1] = temp
    return bill

def check(wallet, bill):
    if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
        return 1
    else:
        return 0
def change(bill):
    if bill[0] > bill[1]:
        bill[0]//=2
    else:
        bill[1]//=2
    return bill
def solution(wallet, bill):
    answer = 0
    
    while True:
        if check(wallet, bill)==1:
            break
        else:
            bill = rotate(bill)
            if check(wallet, bill)==1:
                break
            else:
                answer+=1
                bill = change(bill)
    
    return answer