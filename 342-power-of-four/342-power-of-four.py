class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        print(n)
        if n==1 or n==4:
            return True
        if n%4!=0:
            return False
        elif n<=0:
            return False
        return self.isPowerOfFour(n=n//4)