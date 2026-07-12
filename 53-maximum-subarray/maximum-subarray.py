class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max_sum=float('-inf')
        current_sum=0
        start=end=temp=0
        for i in range(n):
            current_sum=current_sum+nums[i]
            if current_sum>max_sum:
                max_sum=current_sum
                start=temp
                end=i
            if current_sum<0:
                current_sum=0
                temp=i+1
        return max_sum

            


        
        