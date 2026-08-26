class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge cases: the square root of 0 is 0, and 1 is 1
        if x < 2:
            return x
            
        # Start with a wild guess: x itself 
        # (You could also start with x // 2 to be slightly faster)
        r = x
        
        # Keep updating the guess as long as r * r is too big.
        # Once r * r is less than or equal to x, we have found our integer floor.
        while r * r > x:
            # Newton's Method Formula: r = (r + x / r) / 2
            r = (r + x // r) // 2
            
        return r



        