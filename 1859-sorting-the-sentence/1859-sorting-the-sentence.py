class Solution:
    def sortSentence(self, s: str) -> str:
        list=[]
        words=s.split()
        words.sort(key=lambda x: x[-1])
        for i in words:
            list.append(i[:-1])
        op=" ".join(list)
        return op
        