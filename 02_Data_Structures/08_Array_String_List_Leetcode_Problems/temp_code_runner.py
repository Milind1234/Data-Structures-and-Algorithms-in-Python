def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums
nums = [1,0,3,0,4,5,2,0,1]        
print(moveZeroes(nums))