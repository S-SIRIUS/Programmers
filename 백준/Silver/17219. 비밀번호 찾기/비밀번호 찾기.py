#비밀번호 찾기(실버4)
n, m = map(int, input().split())
sp_dict={}
for i in range(n):
    site, password = map(str, input().split())
    sp_dict[site] = password
for i in range(m):
    print(sp_dict[input().strip()])