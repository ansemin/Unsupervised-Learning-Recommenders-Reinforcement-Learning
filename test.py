
    

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    
    i=0
    for j in range(1, len(nums)): #range function does not include the end value 

        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1,print(nums[:i+1])
removeDuplicates([1,2,2,3,4])