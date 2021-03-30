def twoSum(nums, target):
    memo = {}
    for i in range(len(nums)):
        if nums[i] not in memo:
            result = target - nums[i]
            memo[result] = i
        else:
            return (memo[nums[i]], i)
        
        
target = 6
nums = [1,2,3,4,5]
print(twoSum(nums, target))
