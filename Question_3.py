from typing import List
def findDisappearedNumbers(nums):
    for number in nums:
        index = abs(number) - 1
      
        if nums[index] > 0:
            nums[index] *= -1
      
    missing_numbers = [i + 1 for i, x in enumerate(nums) if x > 0]
    print(missing_numbers)

nums = [4,3,2,7,8,2,3,1]
findDisappearedNumbers(nums)