# DNA 비밀번호(실버2)
import sys
input = sys.stdin.readline
def check(needs, state):
    answer=0
    for i in range(4):
        if needs[i] <= state[i]:
            answer+=1
    if answer == 4:
        return True
    else:
        return False
    
dna_len, str_len = map(int, input().split())
dna = list(input())
needs = list(map(int, input().split()))
start=0
end = str_len-1
state = [0]*(4)
total=0
for i in range(start, end+1):
    if dna[i] == 'A':
        state[0]+=1
    elif dna[i] == 'C':
        state[1]+=1
    elif dna[i] == 'G':
        state[2]+=1
    else:
        state[3]+=1

if check(needs, state):
    total+=1

while end < dna_len-1:
    
    if dna[start]=='A':
        state[0]-=1
    elif dna[start]=='C':
        state[1]-=1
    elif dna[start]=='G':
        state[2]-=1
    else:
        state[3]-=1
    
    start+=1
    end+=1
    if dna[end] == 'A':
        state[0]+=1
    elif dna[end] == 'C':
        state[1]+=1
    elif dna[end] == 'G':
        state[2]+=1
    else:
        state[3]+=1
    
    if check(needs, state):
        total+=1

print(total)