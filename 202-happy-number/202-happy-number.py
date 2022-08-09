class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while True:
            res = 0
            while n:
                r = n%10
                n//=10
                res += (r**2)
            
            if res == 1: return True
            
            if res in d: return False
            d.add(res)
            n = res
            
        