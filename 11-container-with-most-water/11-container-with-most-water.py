class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        count=0
        while i<=j:
            value=min(height[i],height[j])*abs(j-i)
            if value>=count:
                count=value
            # print(count)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return count
            
        