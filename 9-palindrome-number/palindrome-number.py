class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        count=0
        if x<0:
            x=-1*x
            count=count+1   
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if (-2**31) < rev <(2**31-1):
            if count == 1:
                return False
            else:
                rev=rev
        else:
            rev=0
        if n == rev:
            return True
        else:
            return False

        