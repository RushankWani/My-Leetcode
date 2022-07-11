class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list=[str(i) for i in s.split()]
        return len(list[-1])