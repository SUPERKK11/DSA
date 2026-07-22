class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        count_max=0
        for i in nums:
            if i == 1:
                count=count+1
            else:
                count=0
            if count>=count_max:
                count_max=count
        return count_max


