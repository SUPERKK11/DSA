class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        count=0
        if x<0:
            x=-1*x
            count=count+1
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if (-2**31) < rev < (2**31-1):
            if count == 1:
                return -1*rev
            else:
                return rev
        else:
            return 0
        