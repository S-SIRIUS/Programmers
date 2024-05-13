def solution(nums):
    new_nums = set(nums)
    if(len(new_nums) < len(nums)//2):
        return len(new_nums)
    else:
        return len(nums)//2