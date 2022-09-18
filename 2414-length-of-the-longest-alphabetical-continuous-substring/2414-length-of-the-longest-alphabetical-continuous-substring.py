class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        alpha={"a":1, "b":2, "c":3, "d":4, "e":5,"f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q": 17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
        list1=[]
        for i in s:
            if i in alpha:
                list1.append(alpha[i])
        if len(list1)==1:
            return 1
        left,right=0,1
        gcount=0
        while right<len(list1):
            
            while right!=len(list1) and list1[right-1]-list1[right]==-1:
                right+=1
            gcount=max(gcount,right-left)
            left=right
            right+=1
        return gcount