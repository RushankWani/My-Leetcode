class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalList=[[1]]
        for i in range(numRows-1):
            temp=[0]+finalList[-1]+[0]
            localList=[]
            for j in range(len(finalList[-1])+1):
                localList.append(temp[j]+temp[j+1])
            finalList.append(localList)
        return finalList