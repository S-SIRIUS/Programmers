n, money= map(int,input().split())
coin=[]
for i in range(0,n):
    temp=int(input())
    coin.append(temp)
coin.sort(reverse=True)
ans=0
for i in coin:
    if money>=i:
        ans+=money//i
        money = money % i
print(ans)