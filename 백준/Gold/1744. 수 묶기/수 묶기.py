n = int(input())
p_array=[]
m_array=[]
zero=[]
one=[]
total=0
for i in range(n):
    num = int(input())
    if num==1:
        one.append(num)
    elif num >0:
        p_array.append(num)
    elif num <0:
        m_array.append(num)
    elif num==0:
        zero.append(num)

p_array.sort()
m_array.sort(reverse=True)

while len(p_array)>1:
    total += (p_array.pop() * p_array.pop())

if len(p_array)>0:
    total+=(p_array.pop())


while len(m_array)>1:
    total += (m_array.pop()*m_array.pop())

if len(m_array)>0:
    if len(zero)==0:
        total+=m_array.pop()
    else:
        zero.pop()

total+=sum(one)

print(total)