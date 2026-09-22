class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i,num in enumerate(nums):

            diff=target-num

            if diff in d:
                return [d[diff],i]
                
            d[num]=i