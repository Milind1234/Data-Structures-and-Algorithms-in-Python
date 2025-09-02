
def largestElement(nums):
    largest = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest
            

def largestElement_1(nums):
    max1, max2 = float('-inf'), float('-inf')
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max1

nums=[3, 3, 0, 99, -40]
print(largestElement(nums))
print(largestElement_1(nums))
            