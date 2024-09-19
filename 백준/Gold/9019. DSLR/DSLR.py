from collections import deque
import sys
input=sys.stdin.readline
def cD(x):
    if(2*x > 9999):
        return (2*x)%10000
    else:
        return 2*x

def cS(x):
    if x==0:
        return 9999
    else:
        return x-1

def cL(x):
    x=str(x)
    temp=""
    temp="0"*(4-len(x))+str(x)
    newtemp=temp[1:4]+temp[0]
    return  int(newtemp)
def cR(x):
    x=str(x)
    temp=""
    temp="0"*(4-len(x))+str(x)
    newtemp=temp[3]+temp[0:3]
    return  int(newtemp)


def bfs(start, obj):
    que=deque()
    que.append(start)
    while que:
        x=que.popleft()
        if(x==obj):
            return
        D=cD(x)
        S=cS(x)
        L=cL(x)
        R=cR(x)
        dic={D:'D',S:'S',L:'L',R:'R'}
        for v in (D, S, L, R):
            if(visited[v]=="" and v!=x):
                visited[v]=visited[x]+dic[v]
                que.append(v)

n=int(input())
for i in range(0, n):
    visited=[""]*(10001)
    start, obj = map(int,input().split())
    bfs(start, obj)
    print(visited[obj])