#perfect solution possible
#here the 1st pointer is at laft most point and 2nd pointer is just next to 1st.
"""if we get a loss(-ve) value it means the selling price is less so we move our left pointer to that exact value and increament right pointer by 1."""
"""if we get a profit(+ve) value it means selling price is more than buying price so we make this current profir our max profit and continue our search for best profit by increaming right pointer by 1"""


class Solution(object):
    def maxProfit(self, prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
            

obj=Solution()  
obj.maxProfit([7,1,5,3,6,4])


"""my solution with aan infinite memory space requirement and infinte time for a list of prices where prices=[10000,9999,9998...]"""

list=[]
for x in range(0,len(prices)):
    for y in range(x+1,len(prices)):
        b= prices[y]-prices[x]
        list.append(b)
# print(list)
list.sort()
# print(list)
if list==[]:
    print("0")
elif max(list)<0:
    print('0')

else:
    print(list[-1]) 