class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        init=a
        count=0
        threshold=len(b)+len(init)
        while len(a)<threshold:
            count+=1
            a=init*count
            if b in a:
                return count
        return-1
        