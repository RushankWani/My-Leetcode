class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        flist=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            flist.append(temp)
        return flist
            