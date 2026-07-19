class Solution:
    def check(self, nums: List[int]) -> bool:
        def rotate_r(k,nums):
            nums[:]=nums[::][::-1][:len(nums)-k][::-1] + nums[::][::-1][len(nums)-k:][::-1]
            if nums == sorted(nums):
                return nums
            return []

        def rotate_l(k,nums):
            nums[:]=nums[::][::-1][:k:][::-1] + nums[::][::-1][k::][::-1]
            if nums == sorted(nums):
                return nums
            return []
    
        for i in range(len(nums)):
            if nums == rotate_r(i,nums):
                return True
            elif nums == rotate_l(i,nums):
                return True
        return False
        
            
        