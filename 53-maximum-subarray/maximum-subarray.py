class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max_sum=nums[0]
        current_sum=nums[0]
        start=end=temp=0
        for i in range(1,n):
            if nums[i]>current_sum+nums[i]:
                current_sum=nums[i]
                temp=i
            else:
                current_sum=current_sum+nums[i]
            if current_sum>max_sum:
                max_sum=current_sum
                start=temp
                end=i
        return max_sum


            


        
        