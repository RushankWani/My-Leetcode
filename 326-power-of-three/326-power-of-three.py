class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1 or n==3:
            return True
        if n%3!=0:
            return False
        elif n<=0:
            return False
        return self.isPowerOfThree(n=n//3)
        