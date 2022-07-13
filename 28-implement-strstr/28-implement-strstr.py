class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        count=0
        while count<len(haystack):
            if needle in haystack[count:len(needle)+count]:
                return count
            else:
                count+=1
        return -1