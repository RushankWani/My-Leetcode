class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_of_candies=max(candies)
        list=[]
        for x in candies:
            if x+extraCandies>=max_of_candies:
                list.append(True)
            else:
                list.append(False)
        return list

o=Solution()
o.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)