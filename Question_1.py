def rearrange(nums, length):
    positive_nums = []
    negative_nums = []
        
    for num in nums:
        if num >= 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)
        
    result = []
    positive_index = 0
    negative_index = 0
        
    while positive_index < len(positive_nums) and negative_index < len(negative_nums):
        result.append(positive_nums[positive_index])
        positive_index += 1
        result.append(negative_nums[negative_index])
        negative_index += 1
        
    result.extend(positive_nums[positive_index:])
        
    result.extend(negative_nums[negative_index:])
        
    nums[:] = result[:]

    print("Positivve Index: ", positive_index)
    print("Negetive Index: ", negative_index)

length = 9
nums = [9, 4, -2, -1, 5, 0, -5, -3, 2]

rearrange(nums, length)