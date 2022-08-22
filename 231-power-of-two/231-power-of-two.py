class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 or n==2:
            return True
        if n%2!=0:
            return False
        elif n<=0:
            return False
        return self.isPowerOfTwo(n=n//2)
        