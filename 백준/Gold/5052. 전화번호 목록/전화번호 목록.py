# 전화번호목록(골드4)
t = int(input())
for i in range(t):
    n = int(input())
    phone=[]
    for j in range(n):
        phone.append(input())
    phone.sort()
    flag=0
    for j in range(n-1):
        length = len(phone[j])
        if phone[j] == phone[j+1][:length]:
            flag=1
            print("NO")
            break
    if flag==0:
        print("YES")