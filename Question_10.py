def merge(nums1, m, nums2, n):

    index_nums1 = m - 1
    index_nums2 = n - 1
      
    merge_index = m + n - 1
      
    while index_nums2 >= 0:
        if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
            nums1[merge_index] = nums1[index_nums1]
            index_nums1 -= 1  
        else:
            nums1[merge_index] = nums2[index_nums2]
            index_nums2 -= 1
        merge_index -= 1  

    print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)