# 걸그룹 마스터 준석이(실버3)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
name_group=dict()
group_name=dict()
for i in range(n):
    gn = input()
    g_list=[]
    m_num = int(input())
    for j in range(m_num):
        m_name = input()
        g_list.append(m_name)
        name_group[m_name] = gn
    g_list.sort()
    group_name[gn] = g_list

for i in range(m):
    temp = input()
    case_num = int(input())
    if case_num==0:
        group = group_name[temp]
        for g in group:
            print(g, end="")
    else:
        group = name_group[temp]
        print(group, end="")