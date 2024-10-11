# 공유기 설치(골드4)
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
home_loc = []

for i in range(n):
    home_loc.append(int(input()))
home_loc.sort()

start=1
end=(home_loc[-1] - home_loc[0])
answer=0

while start <= end:
    middle = (start+end)//2
    current_house = home_loc[0]
    installation=1

    for i in range(1, n):
        if home_loc[i] - current_house >= middle:
            installation+=1
            current_house = home_loc[i]
    
    if installation >= c:
        start = middle+1
        answer=middle
    else:
        end = middle-1
print(answer)