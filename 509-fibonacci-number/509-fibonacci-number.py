class Solution:
    def fib(self, n: int) -> int:
        list=[0,1]
        if n>=2:
            for i in range(n-1):
                count=list[0]+list[1]
                list[0]=list[1]
                list[1]=count
            return count
        elif n==0:
            return 0
        else:
            return 1
            
        