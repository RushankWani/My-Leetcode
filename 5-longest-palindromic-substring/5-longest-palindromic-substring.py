class Solution:
    def longestPalindrome(self, s: str) -> str:
        op=""
        oplen=0
        
        for i in range(len(s)):
                l,r=i,i
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>oplen:
                        op=s[l:r+1]
                        oplen=r-l+1
                    l-=1
                    r+=1
                    
                l,r=i,i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>oplen:
                        op=s[l:r+1]
                        oplen=r-l+1
                    l-=1
                    r+=1
        return op
        