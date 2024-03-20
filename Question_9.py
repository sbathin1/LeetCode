from typing import List

def sortedSquares(nums):
    length = len(nums)
      
    result = [0] * length
      
    start_pointer, end_pointer, result_pointer = 0, length - 1, length - 1
      
    while start_pointer <= end_pointer:
        start_square = nums[start_pointer] ** 2
        end_square = nums[end_pointer] ** 2
          
        if start_square > end_square:
            result[result_pointer] = start_square
            start_pointer += 1
        else:
            result[result_pointer] = end_square
            end_pointer -= 1
          
        result_pointer -= 1
    
    print(result)

nums = [-7,-3,2,3,11]
sortedSquares(nums)