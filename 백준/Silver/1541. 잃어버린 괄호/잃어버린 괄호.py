#잃어버린 괄호(실버2)
## 1) 부호가 전부 같은 경우
value = input()
m_value = value.split('-')
for i in range (0, len(m_value)):
    if '+' in m_value[i]:
        p_value = m_value[i].split('+')
        p_sum=0
        for j in p_value:
            p_sum+=int(j)
        m_value[i] = int(p_sum)

m_sum = int(m_value[0])
for i in range (1, len(m_value)):
    m_sum -= int(m_value[i])
print(m_sum)