# N과 M(9)
def back(nums, path, visited, m):
    if len(path)==m:
        print(*path)
        return
    
    before=-1
    
    for i in range(len(nums)):
        if not visited[i] and nums[i] != before:
                visited[i] = True
                back(nums, path + [nums[i]], visited, m)
                visited[i] = False
                before = nums[i]

n, m = map(int, input().split())
nums = list(map(int ,input().split()))
nums.sort()
visited=[False]*(n)
path=[]
back(nums, path, visited, m)
