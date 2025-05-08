# N과M (실버2)
def make(count, answer):
    if count==m:
        print(*answer)
        return
    else:
        for d in data:
            if len(answer)==0 or (answer[-1] <= int(d)):
                answer.append(d)
                make(count+1, answer)
                answer.pop()

n, m = map(int, input().split())
data = list(map(int, input().split()))
data= list(set(data))
data.sort()
make(0, [])