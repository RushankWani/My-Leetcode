class Solution(object):
    def maximumWealth(self, accounts):
        list=[]
        for i in accounts:
            x=0
            for j in i:
                x=x+j
            list.append(x)
        return max(list)
