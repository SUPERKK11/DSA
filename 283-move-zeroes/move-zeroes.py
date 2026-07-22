class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        count_of_zeros=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count]= nums[i]
                count=count+1
            else:
                count_of_zeros=count_of_zeros+1
        for i in range(len(nums)-count_of_zeros,len(nums)):
            nums[i]=0
        return nums
        
        