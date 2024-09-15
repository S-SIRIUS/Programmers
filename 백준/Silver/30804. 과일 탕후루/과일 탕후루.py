# 과일 탕후루(실버2)
def claim(tanghuru, n):
    fruit_count={}
    left=0
    max_length=0
    for right in range(n):
        if tanghuru[right] in fruit_count:
            fruit_count[tanghuru[right]]+=1
        else:
            fruit_count[tanghuru[right]]=1

        while len(fruit_count) > 2:
            fruit_count[tanghuru[left]]-=1
            if fruit_count[tanghuru[left]]==0:
                del fruit_count[tanghuru[left]]
            left+=1
        max_length = max(max_length, right-left+1) 
    return max_length
n = int(input())
tanghuru = list(map(int, input().split()))
print(claim(tanghuru, n))